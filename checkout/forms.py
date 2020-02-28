from django import forms
from .models import Order


# Order and Payment forms for checkout
class PaymentForm(forms.Form):

    MONTH_RANGE = [(i, i) for i in range(1, 12)]
    YEAR_RANGE = [(i, i) for i in range(2020, 2030)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_RANGE, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_RANGE, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'country', 'postcode',
            'town_or_city', 'street_address1', 'street_address2',
            'county'
        )
