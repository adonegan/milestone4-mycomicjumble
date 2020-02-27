from django.test import TestCase
from accounts.forms import LoginForm


class TestForm(TestCase):

    def test_field_must_be_filled_in(self):

        form = LoginForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])