from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def signIn(request):
    return render(request, "userInfo/SignIn.html")

def signUp(request):
    return render(request, "userInfo/SignUp.html")

def Home(request):
    return render(request, "userInfo/Home.html")

