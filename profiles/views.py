from django.shortcuts import render


def profile(request):

    template = 'profiles/user-profile.html'
    context = {}

    return render(request, template, context)
