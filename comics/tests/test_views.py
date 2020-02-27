from django.test import TestCase
from django.shortcuts import get_object_or_404


class TestComicViews(TestCase):

    def test_get_comics_page(self):
        page = self.client.get("/comics/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "comics.html")

    def test_get_search_page(self):
        page = self.client.get("/search/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "search.html")
