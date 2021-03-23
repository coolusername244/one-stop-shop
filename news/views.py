from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms
from .models import News


def news(request):

    news = News.objects.all().order_by('date')

    template = 'news/news.html'
    context = {
        'news': news,
    }

    return render(request, template, context)


@login_required
def add_news(request):
    add_news_form = forms.NewsForm()

    template = 'news/add_news.html'
    context = {
        'add_news_form': add_news_form,
    }

    return render(request, template, context)
