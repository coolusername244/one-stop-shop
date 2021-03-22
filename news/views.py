from django.shortcuts import render


def news(request):
    template = 'news/news.html'
    return render(request, template)
