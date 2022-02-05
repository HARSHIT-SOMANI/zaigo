from . import views
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('fileu',views.fileu,name='fileu'),
    path('register/',RegisterUser.as_view())
    
]
