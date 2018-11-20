from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from django.shortcuts import render
from .models import Contact
from .forms import UserContactForm
import sendgrid
import os


def contact_view(request):

    if request.method == 'POST':
        form = UserContactForm(request.POST)
        if form.is_valid():

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            contact = form.save(commit=False)
            contact.first_name = first_name
            contact.last_name = last_name
            contact.email = email
            contact.message = message

            # Email ourselves the submitted contact message

            client = settings.SEND_GRID_CLIENT
            message = settings.SEND_GRID_MESSAGE

            message.add_to(["Mpho.Maleka@rheinmetall-denelmunition.com", "mpho.maleka3@gmail.com", email])
            message.set_from("nonreply@gearacademy.co.za")
            message.set_subject("Thank You For Contacting Us")
            context = {
                'first_name': first_name,
                'email': email,
                'message': message
            }
            contact_message = get_template('contact/contact_message.html').render(context)
            message.set_html(contact_message)
            client.send(message)

            contact.save()

        return render(request, 'contact/thank_you.html', {'contact': contact})
    else:
        form = UserContactForm()

        context = {
            'form': form,
            'title': 'Contact Us',
            'buttonText': 'Submit'
        }

    return render(request, 'contact/contact.html', context)
