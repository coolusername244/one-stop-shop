from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product


# Create your views here.
def view_shopping_bag(request):
    # This is a view that returns the shopping bag to the user

    return render(request, 'bag/shopping-bag.html')


def add_item_to_bag(request, item_id):
    # This is a view that will allow users to add items to the shopping bag
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {product.name} quantity to'
                    f'{bag[item_id]["items_by_size"][size]}'
                    )
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request,
                    f'Added size {size.upper()} {product.name} to your bag'
                    )
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request,
                f'Added size {size.upper()} {product.name} to your bag'
                )
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {bag[item_id]}'
                )
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def modify_bag(request, item_id):
    # This is a view that will allow users change the quantity of items in the
    # shopping bag

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.info(
                request,
                f'Updated size {size.upper()} {product.name} quantity to'
                f'{bag[item_id]["items_by_size"][size]}'
                )
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.info(
                    request,
                    f'Removed size {size.upper()} {product.name} from your bag'
                    )
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.info(
                request,
                f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.info(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_shopping_bag'))


def delete_item_from_bag(request, item_id):
    # This is a view that will allow users to delete an item in the bag
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.info(
                request,
                f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.info(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
