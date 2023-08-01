from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup,name='signup' ),
    # path('login',vi/ews.login,name='login' ),
]
