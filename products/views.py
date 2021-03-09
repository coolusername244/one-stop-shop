from django.shortcuts import render, get_object_or_404
from .models import Product


def products_library(request):
    # This is the view that will return all of the products
    # and have sorting functions

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def single_product_detail(request, product_id):
    # This is a view that will return the information for an
    # individual product

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/single_product_detail.html', context)
