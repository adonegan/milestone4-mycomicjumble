from django.test import TestCase
from .forms import LoginForm


class TestViews(TestCase):

    def test_get_login_page(self):

        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")


class TestForm(TestCase):

    def test_field_must_be_filled_in(self):

        form = LoginForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])
