from django.shortcuts import render
from .models import Product


def products_library(request):
    # This is the view that will return all of the products
    # and have sorting functions

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
