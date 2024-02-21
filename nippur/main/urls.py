from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('home', views.index, name = "index"),
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
    path('index', views.index, name = "index"),
]

