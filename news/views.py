from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms
from .models import News
from .forms import NewsForm


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


@login_required
def edit_news(request, news_id):

    if not request.user.is_superuser:
        messages.error(request,
                       'You do not have permission to carry out this task')
        return redirect(reverse('news'))

    news = get_object_or_404(News, pk=news_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article Updated Successfully!')
            return redirect('news')
        else:
            messages.error(request,
                           'Failed to update. Check the form is valid.')
    else:
        form = NewsForm(instance=news)
        messages.info(request, f'You are about to edit { news.title }')

    template = 'news/edit_news.html'
    context = {
        'form': form,
        'news': news
    }

    return render(request, template, context)


@login_required
def delete_news(request, news_id):

    if not request.user.is_superuser:
        messages.error(request,
                       'You do not have permission to carry out this task')
        return redirect(reverse('news'))

    product = get_object_or_404(News, pk=news_id)
    product.delete()
    messages.success(request, 'Article has been removed from the board!')
    return redirect(reverse('news'))
