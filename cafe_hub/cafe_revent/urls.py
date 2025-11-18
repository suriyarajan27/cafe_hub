from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.sign, name="sign"),
    path('login', views.login, name="login")
]
