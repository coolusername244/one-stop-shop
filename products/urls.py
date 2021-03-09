from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_library, name='products'),
    path('<product_id>', views.single_product_detail, name='single_product_detail'),
]
