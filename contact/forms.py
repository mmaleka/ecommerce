from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper


class UserContactForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'message']
