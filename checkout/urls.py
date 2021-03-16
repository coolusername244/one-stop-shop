from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_complete/<order_number>', views.checkout_complete, name='checkout_complete'),
]
