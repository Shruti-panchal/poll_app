from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('homepage/', views.homepage, name="homepage"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('create/', views.create, name="create"),
    path('vote/<poll_id>/', views.vote, name="vote"),
    path('result/<poll_id>/', views.result, name="result"),
]
