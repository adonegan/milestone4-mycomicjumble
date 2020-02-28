from django.test import TestCase
from comics.models import Comic


class TestCartViews(TestCase):
    """
    Get cart page and status of 200
    """

    def test_get_cart_page(self):
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")
