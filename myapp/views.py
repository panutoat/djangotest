
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,Group
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.cache import cache
from django.db import connection
from .forms import LoginForm
from . database import * 
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied

def home(request): 
    return render(request, 'home.html')

@login_required
@permission_required('myapp.Can_view_page', raise_exception=True)
def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.user.groups.filter(name='Viewer').exists(): 
        return render(request, 'contact.html')
    else:
        raise PermissionDenied("You don't have permission to access this page.")
    

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



@login_required
def product(request):
    # Check if search query is submitted
    search_query = request.GET.get('product_code')
    sort_by = request.GET.get('sort')
    print(sort_by)
    if search_query is not None:
        data = query_db(f"SELECT * FROM demo.tb_product WHERE product_code LIKE '%{search_query}'")
        cache.set('product_data', data, timeout=3600)
    else:
        cached_data = cache.get('product_data')
        if cached_data is not None:  
            data = cached_data
        else:
            data = query_db('SELECT * FROM demo.tb_product limit 100')
            cache.set('product_data', data, timeout=3600)
    if sort_by:
        data = sorted(data, key=lambda x: x[sort_by], reverse=False)
        cache.set('product_data', data, timeout=3600)
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product.html', {'page_obj': page_obj})




def add_product(request):
    if request.method == 'POST':
        product_code = request.POST.get('product_code')
        product_name = request.POST.get('product_name')
        product_type = request.POST.get('product_type')
        amount = request.POST.get('amount')
        
        query = f'''INSERT INTO demo.tb_product (product_code, product_name, product_type,amount) VALUES ('{product_code}', '{product_name}', '{product_type}','{amount}')'''
        query_to_db(query=query)
        
        return redirect('product')  
    else:
        return redirect('product')  
def edit_product(request):
    print('1111111111111111111111111111')
    if request.method == 'POST':
        product_code = request.POST.get('product_code')
        product_name = request.POST.get('product_name')
        product_type = request.POST.get('product_type')
        amount = request.POST.get('amount')
        
        query = f'''update demo.tb_product 
        set 
        product_name ='{product_name}',
        product_type ='{product_type}',
        amount ='{amount}',
        where product_code = '{product_code}'
        '''
        query_to_db(query=query)
        
        return redirect('product')  
    else:
        return redirect('product')    