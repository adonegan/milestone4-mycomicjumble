from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import index, about_view, contact_view, glossary_view, privacy_view, terms_view, faqs_view


class TestHomeUrls(SimpleTestCase):
    """Tests that all urls in Home app correspond to the correct view"""

    def test_index_view_url_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_about_view_url_is_resolved(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about_view)

    def test_contact_view_url_is_resolved(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact_view)

    def test_glossary_view_url_is_resolved(self):
        url = reverse('glossary')
        self.assertEqual(resolve(url).func, glossary_view)

    def test_privacy_view_url_is_resolved(self):
        url = reverse('privacy')
        self.assertEqual(resolve(url).func, privacy_view)

    def test_terms_view_url_is_resolved(self):
        url = reverse('terms')
        self.assertEqual(resolve(url).func, terms_view)

    def test_glossary_view_url_is_resolved(self):
        url = reverse('faqs')
        self.assertEqual(resolve(url).func, faqs_view)
