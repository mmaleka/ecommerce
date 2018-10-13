from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .models import Contact
from .forms import UserContactForm


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

            subject  = 'Contact Form Received'
            from_email = settings.EMAIL_HOST_USER
            to_email = ['mpho.maleka3@gmail.com']

            some_html_message = """<p>This is an <strong>important</strong> message.</p>"""

            contact_message = "{0}, from {1} with email {2}".format(message, first_name, email)

            send_mail(subject, contact_message, from_email, to_email, html_message=some_html_message, fail_silently=False)

            # send_mail('Subject here', 'Here is the message.', 'mpho.maleka3@gmail.com', ['mpho.maleka3@gmail.com'], fail_silently=False)

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
