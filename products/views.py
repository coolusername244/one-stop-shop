from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product


def products_library(request):
    # This is the view that will return all of the products
    # and have sorting and searching functions

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                messages.error(request, "One must know what one is looking for")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

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
