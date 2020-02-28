from django.test import TestCase
from comics.models import Comic


class ComicModelTest(TestCase):
    """Tests string for comic names and primary key of details page"""

    def test_string_representation(self):
        comic = Comic(name="Spider-Man (2019) #1")
        self.assertEqual(str(comic), comic.name)

    def test_details_url(self):
        pk = 2
        name = "Spider-Man (2019) #1"
        expected_result = '/comics/details/' + str(pk)
        comic = Comic(pk=pk, name=name)
        result = '/comics/details/2'
        self.assertEqual(result, expected_result)
