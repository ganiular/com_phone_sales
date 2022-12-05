from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('product', views.product, name='product'),
    path('product/<int:product_id>', views.product, name='product'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('add_to_cart/<int:product_id>/<page>', views.add_to_cart, name='add_to_cart'),
    path('remove_cart_item/<int:product_id>/<page>', views.remove_cart_item, name='remove_cart_item')
]