from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_info in bag.items():
        if isinstance(item_info, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_info * product.price
            product_count += item_info
            bag_items.append({
                'item_id': item_id,
                'quantity': item_info,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_info['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return context
