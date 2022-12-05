from django.shortcuts import render, redirect
from .models import Phone, Cart

# Create your views here.
def shop(request):
    return render(request, 'shop.html')

def product(request, product_id=1):
    context = {
        'product': Phone.objects.get(id=product_id),
        'products': Phone.objects.all()
    }
    return render(request, 'single-product.html', context)

def cart(request):
    context = {
        'cart_items': Cart.objects.all()
    }
    return render(request, 'cart.html', context)

def checkout(request):
    return render(request, 'checkout.html')

def add_to_cart(request, product_id, page):
    try:
        cart = Cart.objects.get(phone__id=product_id) 
        cart.quantity += 1 # increase quantity
        cart.save()
    except Cart.DoesNotExist:    
        phone = Phone.objects.get(id=product_id)
        cart = Cart(phone=phone, quantity=1)
        cart.save()
    if(page == 'product'):
        return redirect(page, product_id=product_id)
    return redirect(page)

def remove_cart_item(request, product_id, page):
    item = Cart.objects.get(phone__id=product_id)
    item.delete()
    return redirect(page)