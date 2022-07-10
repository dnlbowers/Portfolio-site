from django.test import TestCase

# Create your tests here.
class TestPage(TestCase):
    
    def test_Portfolio_page(self):
        response = self.client.get("/portfolio/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "portfolio/portfolio.html")