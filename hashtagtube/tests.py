from django.test import TestCase
from django.urls import reverse

class IndexViewTests(TestCase):
	def test_index_view_with_no_categories(self):
		"""
		If no categories exist, the appropriate message should be displayed.
		"""
		response = self.client.get(reverse('hashtagtube:index'))

		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context['categories'], [])
