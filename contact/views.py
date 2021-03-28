from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from . import forms


def contact(request):
    """
    This view will allow users to send messages to site admin
    """
    if request.method == 'POST':
        contact_form = forms.ContactForm(request.POST)
        from_email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('body', '')

        if contact_form.is_valid():
            contact_form.save()
            send_mail(
               subject,
               message,
               from_email,
               ['leesheppard2404@gmail.com'],
            )
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
