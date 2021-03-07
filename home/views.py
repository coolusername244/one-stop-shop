from django.shortcuts import render


# Create your views here.
def index(request):
    # This is a view that returns index.html

    return render(request, 'home/index.html')
