from django.shortcuts import render
from .models import Contact
from .forms import UserContactForm


def contact_view(request):

    if request.method == 'POST':
        form = UserContactForm(request.POST)
        print("is form valid", form)
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
