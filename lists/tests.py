from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

	def test_url_resolves_to_homepage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)