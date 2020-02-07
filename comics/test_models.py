from django.test import TestCase
from .models import Comic


class ComicSubmitTest(TestCase):
    """ To test Comic model returns comic name """
    def test_test_title(self):
        comic = Comic(name="Comic")
        self.assertEqual(str(comic), comic.name)
