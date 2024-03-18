

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.cache import cache
from django.db import connection
from .forms import LoginForm
from . database import * 



def home(request): 
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username_login')
        password = request.POST.get('password_login')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            request.session['username'] = username
            return redirect('user_page')  
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def user_page(request):
    # Make sure the user is logged in
    if request.user.is_authenticated:
        # Get username from session
        username = request.session.get('username')
        return render(request, 'user_page.html', {'username': username})
    else:
        # Redirect to login page if the user is not logged in
        return redirect('login')
def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return HttpResponseRedirect('/')  
    else:
        return render(request, 'login.html')    
def user_logout(request):
    del request.session['username']
    logout(request)
    return redirect('home')    




def product(request):
    cached_data = cache.get('product_data')
    if cached_data:
        data = cached_data
    else:
        data = query_db('select * from demo.tb_product')
        cache.set('product_data', data, timeout=3600)

    paginator = Paginator(data, 10) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product.html', {'page_obj': page_obj})