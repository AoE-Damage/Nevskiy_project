from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.mainpage, name="main"),
    path("choosing-apartments/", views.home, name="home"),
    path("building/", views.building, name="building"),
]
