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

    class Meta:
        model = Order
        fields = ['address', 'postal_code', 'city', 'payment_method']
