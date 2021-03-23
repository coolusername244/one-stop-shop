from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms
from .models import News


def news(request):

    news = News.objects.all().order_by('-date')

    template = 'news/news.html'
    context = {
        'news': news,
    }

    return render(request, template, context)


@login_required
def add_news(request):

    if not request.user.is_superuser:
        messages.error(request,
                       'You do not have permission to carry out this task.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        add_news_form = forms.NewsForm(request.POST, request.FILES)
        if add_news_form.is_valid():
            instance = add_news_form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, 'News article added successfully!')
            return redirect('news')
    else:
        add_news_form = forms.NewsForm()

    template = 'news/add_news.html'
    context = {
        'add_news_form': add_news_form,
    }

    return render(request, template, context)
