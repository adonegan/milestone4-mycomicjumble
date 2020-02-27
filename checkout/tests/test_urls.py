from django.test import SimpleTestCase
from django.urls import reverse, resolve
from checkout.views import checkout


class TestUrls(SimpleTestCase):

    def test_checkout_view_url_is_resolved(self):
        url = reverse('checkout')
        self.assertEqual(resolve(url).func, checkout)
