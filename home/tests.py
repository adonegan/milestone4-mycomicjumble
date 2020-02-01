from django.test import TestCase
from django.shortcuts import get_object_or_404


class TestViews(TestCase):

    def test_index_is_rendered(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
