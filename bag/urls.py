from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.view_shopping_bag,
         name='view_shopping_bag'
         ),
    path('add/<item_id>/',
         views.add_item_to_bag,
         name='add_item_to_bag'
         ),
    path('modify/<item_id>/',
         views.modify_bag,
         name='modify_bag'
         ),
    path('remove/<item_id>/',
         views.delete_item_from_bag,
         name='delete_item_from_bag'
         ),
]
