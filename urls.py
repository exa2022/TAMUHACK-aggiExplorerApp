from django.urls import path
from .import views

urlpatterns = [
    path('signin',views.signIn),
    path('signup',views.signUp),
    path('home', views.Home),
]
