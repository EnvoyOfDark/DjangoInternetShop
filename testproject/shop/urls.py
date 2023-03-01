from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='from'),
    path('category/', views.category, name='category'),
    path('product/', views.product, name='product'),
]