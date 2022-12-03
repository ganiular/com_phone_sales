# Create project
    django-admin startproject phone_sales

# cd into the project folder
    cd phone_sales

# create main app
    python manage.py startapp main

# create template folder
    mkdir templates

# Copy file template
Copy all the contents in the sample template (ustora) to the template folder we created

# Register templates files location
Open phone_sales/settings find TEMPLATES list and edit the following line as

    'DIRS': [BASE_DIR/'templates'],

# Create index view
open main/views.py file create index view and render the index.html template

    def index(request):
        return render(request, "index.html")

# Create url pattern
Create main/urls.py file to include the followind lines of code

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index), 
    ]

# Link urls
Open phone_sales/urls.py file to link the urlpatterns in main/urls.py 
with the one in phone_sales/urls.py
    
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]

# Register the app
open phone_sales/settings.py find INSTALLED_APPS list and inlude 'main' in the list

# Run Project
    python manage.py runserver
Open browers and browse this link http://127.0.0.1:8000/. If you follow the right process your project should run succesfully.
You will notice the webpage is not styled. Let continue on how to style the webpage. Stop the running app with <kbd>Ctrl</kbd>+<kbd>C</kbd>

# Create static folder
    mkdir static

# Copy static files
Move the following folders from templates folder to the static folder
 * css
 * fonts
 * img
 * js

# Register static files and urls
Open phone_sales/settings.py and change the line of codes as

    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        BASE_DIR / 'static',
    ]

# Embed the static files into the template
Open the templates/index.html and follow the following instructions
 1. type the `{% load static %}` on the first line
 
 2. surround all static urls starting with _`"css/..."`_ with `{% static '' %}`.For example `"css/bootstrap.min.css"` will be `"{% static 'css/bootstrap.min.css' %}"`.<br>

    > To rplace all at once, click <kbd>Ctrl</kbd>+<kbd>H</kbd>. Click <kbd>Alt</kbd>+<kbd>R</kbd>. Insert `('|")(css/.*?)\1` in the find input. Insert `$1{% static '$2' %}$1` in the replace input. Then click **Replace All** button.

    > In the find input, insert the following strings and click replace all one each.
     * ('|")(js/.*?)\1
     * ('|")(img/.*?)\1
     * ('|")(fonts/.*?)\1



# Create product app
    python manage.py startapp product

# create shop and product views
    def shop(request):
        return render(request, 'shop.html')

    def product(request):
        return render(request, 'single-product.html')

# Create url pattern
Create product/urls.py file to include the followind lines of code

    from django.urls import path
    from . import views

    urlpatterns = [
        path('shop', views.shop),
        path('product', views.product),
    ]

# Link urls
Open phone_sales/urls.py file to link the urlpatterns in products/urls.py 
with the one in phone_sales/urls.py
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
        path('', include('product.urls')),
    ]

# Register the app
open phone_sales/settings.py find INSTALLED_APPS list and inlude 'product' in the list

# Embed the static files into the template
We are going to repeat the same process we did to embed static files into index.html for shop.html and single-product.html