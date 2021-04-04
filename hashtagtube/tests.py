from django.test import TestCase
from django.urls import reverse
from hashtagtube.models import Category

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
		self.assertEquals(num_categories, 3)

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
		self.assertEquals(num_categories, 3)		

def add_category(title):
	category = Category.objects.get_or_create(title=title)[0]
	
	category.save()
	return category

