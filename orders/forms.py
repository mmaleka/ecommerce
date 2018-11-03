from django import forms
from .models import Order
from crispy_forms.helper import FormHelper


class OrderCreateForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    payment_Choices = (
    ('EP', 'EFT Payment'),
    ('DP', 'Payment on delivery'),
    )

    shipping_Choices = (
    ('FD', 'Free delivery (Free) - 20 to 37 days'),
    ('PL', 'Priority delivery (R 40.00) - 4 to 15 days'),
    )

    class Meta:
        model = Order
        fields = ['address', 'postal_code', 'city', 'shipping', 'payment_method']
