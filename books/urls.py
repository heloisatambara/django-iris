from django.contrib import admin
from django.urls import path, include
from .views import home, save

urlpatterns = [
    path('', home),
    path('save/', save, name="save"),
]