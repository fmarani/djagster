from django.urls import reverse
from django_webtest import WebTest


class TestPage(WebTest):
    def test_home_page_works(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
