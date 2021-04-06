from django.test import TestCase
from django.urls import reverse
from hashtagtube.models import Category, Page, UserProfile
from django.contrib.auth.models import User
from django.test import Client
from hashtagtube.forms import CategoryForm

class CategoryMethodTests(TestCase):
	def test_slug_line_creation(self):
		"""
		Checks to make sure that when a category is created, an 
		appropriate slug is created.
		Example: "Random Category String" should be "random-category-string".
		"""
		category = add_category('Random Category String')

		self.assertEqual(category.slug, 'random-category-string')


class PageMethodTests(TestCase):
	def test_ensure_views_are_positive(self):
		user = add_user('author1', 'author1@gmail.com', 'authorpassword')
		author = add_user_profile(user, 'profile_pic.jpg')
		category = add_category('Music')
		page = add_page('title', author, category, 'video.mp4', 'thumbnail.jpg', views=-1) 

		self.assertEqual((page.views >= 0), True)

	def test_ensure_like_react_is_postive(self):
		user = add_user('author1', 'author1@gmail.com', 'authorpassword')
		author = add_user_profile(user, 'profile_pic.jpg')
		category = add_category('Sport')
		page = add_page('title', author, category, 'video.mp4', 'thumbnail.jpg', like_react=-1)

		self.assertEqual((page.like_react >= 0), True)

	def test_ensure_dislike_react_is_positive(self):
		user = add_user('author1', 'author1@gmail.com', 'authorpassword')
		author = add_user_profile(user, 'profile_pic.jpg')
		category = add_category('Music')
		page = add_page('title', author, category, 'video.mp4', 'thumbnail.jpg', dislike_react=-1)

		self.assertEqual((page.dislike_react >= 0), True)

	def test_ensure_haha_react_is_positive(self):
		user = add_user('author1', 'author1@gmail.com', 'authorpassword')
		author = add_user_profile(user, 'profile_pic.jpg')
		category = add_category('Music')
		page = add_page('title', author, category, 'video.mp4', 'thumbnail.jpg', haha_react=-1)

		self.assertEqual((page.haha_react >= 0), True)
	
	def test_ensure_love_react_is_positive(self):
		user = add_user('author1', 'author@gmail.com', 'authorpassword')
		author = add_user_profile(user, 'profile_pic.jpg')
		category = add_category('Music')
		page = add_page('title', author, category, 'video.mp4', 'thumbnail.jpg', love_react=-1)
	
		self.assertEqual((page.love_react >= 0), True)


class IndexViewTests(TestCase):
	def test_index_view_with_no_categories(self):
		response = self.client.get(reverse('hashtagtube:index'))

		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context['categories'], [])
	
	def test_index_view_with_categories(self):
		"""
		Checks whether categories are displayed correctly when present.
		"""
		add_category('Music')
		add_category('Sport')
		add_category('Food')

		response = self.client.get(reverse('hashtagtube:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Music")
		self.assertContains(response, "Sport")
		self.assertContains(response, "Food")

		num_categories = len(response.context['categories'])
		self.assertEqual(num_categories, 3)


class ProfileViewTests(TestCase):
	def test_profile_view_without_categories(self):
		response = self.client.get(reverse('hashtagtube:profile'))

		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context['categories'], [])

	def test_profile_view_with_categories(self):
		"""
		Checks whether categories are displayed correctly when present.
		"""
		add_category('Music')
		add_category('Sport')
		add_category('Food')

		response  = self.client.get(reverse('hashtagtube:profile'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Music")
		self.assertContains(response, "Sport")
		self.assertContains(response, "Food")

		num_categories = len(response.context['categories'])
		self.assertEqual(num_categories, 3)

	def test_profile_view_with_no_pages(self):
		response = self.client.get(reverse('hashtagtube:profile'))

		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context['pages'], [])

	def test_profile_view_with_pages(self):
		author = add_user_profile(add_user('John123', 'john@gmail.com', 'johnpassword'), 'profileImage.jpg')
		category = add_category('Music')

		add_page('Page1', author, category, 'video.mp4', 'image.jpg')

		response = self.client.get(reverse('hashtagtube:profile'))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context['pages'], ['Page1'])


class ShowCategoryViewTests(TestCase):
	def test_show_category_view_when_category_exists(self):
		category = add_category('Food')

		response = self.client.get(reverse('hashtagtube:show_category', args=['food']))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Food')
		self.assertEqual(response.context['category'], category)

	def test_show_category_view_when_category_does_not_exist(self):
		response = self.client.get(reverse('hashtagtube:show_category', args=['food']))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['pages'], None)
		self.assertEqual(response.context['category'], None)


class VideoViewTests(TestCase):
	def test_video_view_with_invalid_video_id(self):
		response = self.client.get(reverse('hashtagtube:video', args=['1000000']))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed('hashtagtube/notFound.html')


class RestrictedViewTests(TestCase):
	def test_restricted_view(self):
		user = User.objects.create(username='testuser')
		user.set_password('12345')
		user.save()

		self.client.login(username='testuser', password='12345')
		response = self.client.get(reverse('hashtagtube:restricted'))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['boldmessage'], "Since you're logged in, you can see this text!")


class AddCategoryViewTests(TestCase):
	def test_add_category_view_by_adding_category(self):
		user = User.objects.create(username='testuser')
		user.set_password('12345')
		user.save()

		self.client.login(username='testuser', password='12345')
		response = self.client.post(reverse('hashtagtube:add_category'), data={'title':'Example Category'})

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Example Category")


def add_category(title):
	category = Category.objects.get_or_create(title=title)[0]

	category.save()
	return category

def add_page(title, author, category, video, thumbnail, views=0, like_react=0, dislike_react=0, haha_react=0, love_react=0):
	page = Page.objects.get_or_create(title=title, author=author, category=category, 
	       video=video, thumbnail=thumbnail, views=views, like_react=like_react, dislike_react=dislike_react, haha_react=haha_react,
	       love_react=love_react)[0]

	return page

def add_user_profile(user, picture):
	user_profile = UserProfile.objects.get_or_create(user=user, picture=picture)[0]

	return user_profile

def add_user(username, email, password):
	user = User.objects.create_user(username=username, email=email, password=password)

	user.save()
	return user
