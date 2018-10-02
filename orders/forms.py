from django import forms
from .models import Order
from crispy_forms.helper import FormHelper


class OrderCreateForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    class Meta:
        model = Order
        fields = ['address', 'postal_code', 'city']
