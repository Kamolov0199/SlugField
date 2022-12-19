from django.contrib import admin
from .views import home, detal
from django.urls import path

urlpatterns = [
    path('', home),
    path('<slug:slug>/', detal, name='detal')
]
