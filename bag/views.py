from django.shortcuts import render


# Create your views here.
def view_shopping_bag(request):
    # This is a view that returns the shopping bag to the user

    return render(request, 'bag/shopping-bag.html')
