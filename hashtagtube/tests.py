from django.test import TestCase
from django.urls import reverse
from hashtagtube.models import Category, Page, UserProfile
from django.contrib.auth.models import User

class CategoryMethodTests(TestCase):
	def test_slug_line_creation(self):
		"""
		Checks to make sure that when a category is created, an 
		appropriate slug is created.
		Example: "Random Category String" should be "random-category-string".
		"""
		category = add_category('Random Category String')

		self.assertEqual(category.slug, 'random-category-string')

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
	def test_profile_view_with_no_categories(self):
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
		self.assertContains(response, "Page1")

		num_pages = len(response.context['pages'])
		self.assertEqual(num_pages, 3)

def add_category(title):
	category = Category.objects.get_or_create(title=title)[0]

	category.save()
	return category

def add_page(title, author, category, video, thumbnail):
	page = Page.objects.get_or_create(title=title, author=author, category=category, 
	       video=video, thumbnail=thumbnail)[0]
	
	return page

def add_user_profile(user, picture):
	user_profile = UserProfile.objects.get_or_create(user=user, picture=picture)[0]

	return user_profile

def add_user(username, email, password):
	user = User.objects.create_user(username=username, email=email, password=password)
	
	user.save()
	return user
