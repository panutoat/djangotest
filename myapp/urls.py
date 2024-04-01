# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user/', views.user_page, name='user_page'),
    path('create_user/', views.create_user, name='create_user'),
    path('product/', views.product, name='product'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/', views.add_product, name='edit_product'),
]
