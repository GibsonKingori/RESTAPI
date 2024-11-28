from django.urls import path
from .views import create_product, list_products

urlpatterns = [
    path('products/', list_products, name='list_products'),
    path('products/create/', create_product, name='create_product'),
]