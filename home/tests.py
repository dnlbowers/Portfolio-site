from django.test import TestCase

# Create your tests here.
class TestPage(TestCase):
    
   def setUp(self):
       self.client = Client()

   def test_index_page(self):
       url = reverse('index')
       response = self.client.get(url)
       self.assertEqual(response.status_code, 200)
       self.assertTemplateUsed(response, 'index.html')
       self.assertContains(response, 'Company Name XYZ')