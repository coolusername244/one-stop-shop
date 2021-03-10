from django.shortcuts import render, redirect


# Create your views here.
def view_shopping_bag(request):
    # This is a view that returns the shopping bag to the user

    return render(request, 'bag/shopping-bag.html')


def add_item_to_bag(request, item_id):
    # This is a view that will allow users to add items to the shopping bag
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag


    return redirect(redirect_url)
