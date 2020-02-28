from django.test import SimpleTestCase
from django.urls import reverse, resolve
from comics.views import all_comics


class TestUrls(SimpleTestCase):
    """
    Tests that comics url in Comics app corresponds to correct view
    """

    def test_comics_view_url_is_resolved(self):
        url = reverse('comics')
        self.assertEqual(resolve(url).func, all_comics)
