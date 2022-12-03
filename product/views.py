from django.shortcuts import render

# Create your views here.
def shop(request):
    return render(request, 'shop.html')

def product(request):
    return render(request, 'single-product.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')