from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string
from lists.models import Item

# Create your tests here.

class HomePageTest(TestCase):

	def test_url_resolves_to_homepage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)
	
	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)
	
	def do_post_request_with_new_item(self, item_text):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item'
		return home_page(request)
	
	def test_homepage_can_save_a_post_request(self):
		item_text = 'A new list item'
		response = self.do_post_request_with_new_item(item_text)
		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new list item')
	
	def test_homepage_can_redirect_after_a_post_request(self):
		response = self.do_post_request_with_new_item('irrelevant name')
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')
	
	def test_saving_and_retrieving_items(self):
		first_item = Item()
		first_item.text = 'The first list item (like ever)'
		first_item.save()
		
		second_item = Item()
		second_item.text = 'Item the second'
		second_item.save()
		
		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)
		
		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'The first list item (like ever)')
		self.assertEqual(second_saved_item.text, 'Item the second')
		
	def test_homepage_only_saves_when_necessary(self):
		request = HttpRequest()
		home_page(request)
		self.assertEqual(Item.objects.count(), 0)
		
	def test_home_page_displays_all_list_items(self):
		Item.objects.create(text='my item 1')
		Item.objects.create(text='my item 2')
		request = HttpRequest()
		response = home_page(request)
		self.assertIn('my item 1', response.content.decode())
		self.assertIn('my item 2', response.content.decode())