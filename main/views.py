from django.shortcuts import render
from product.models import Phone

# Create your views here.
def index(request):
    context = {
        'products': Phone.objects.all()
    }
    return render(request, "index.html", context)