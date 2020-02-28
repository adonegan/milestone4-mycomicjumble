from django.test import TestCase
from django.shortcuts import get_object_or_404


class TestHomeViews(TestCase):
    """
    Gets all pages in Home app with page status of 200
    """

    def test_index_is_rendered(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_about_is_rendered(self):
        page = self.client.get("/about/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "about.html")

    def test_contact_is_rendered(self):
        page = self.client.get("/contact/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "contact.html")

    def test_faqs_is_rendered(self):
        page = self.client.get("/faqs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "faqs.html")

    def test_glossary_is_rendered(self):
        page = self.client.get("/glossary/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "glossary.html")

    def test_privacy_is_rendered(self):
        page = self.client.get("/privacy/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "privacy.html")

    def test_termsandcond_is_rendered(self):
        page = self.client.get("/terms/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "terms.html")
