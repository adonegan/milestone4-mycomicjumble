from django.test import SimpleTestCase
from django.urls import reverse, resolve
from comics.views import all_comics


class TestUrls(SimpleTestCase):

    def test_comics_view_url_is_resolved(self):
        url = reverse('comics')
        self.assertEqual(resolve(url).func, all_comics)
