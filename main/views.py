from django.shortcuts import render
from product.models import Phone
from .models import Member

# Create your views here.
def index(request):
    context = {
        'products': Phone.objects.all()
    }
    return render(request, "index.html", context)

def contact(request):
    context = {
        'members': Member.objects.all()
    }
    return render(request, 'contact.html', context)