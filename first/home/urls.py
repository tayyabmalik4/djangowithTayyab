from unicodedata import name
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about, name='about'),
    path('contect',views.contect, name='contect') ,
]