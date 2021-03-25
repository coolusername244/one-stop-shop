from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms


def contact(request):

    if request.method == 'POST':
        contact_form = forms.ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.info(request,
                          'Your message has been sent to our admin!')
            return redirect('home')
    else:
        contact_form = forms.ContactForm()

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form
    }

    return render(request, template, context)
