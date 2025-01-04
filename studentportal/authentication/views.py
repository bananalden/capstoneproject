from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'login/login.html')

def unauthorized_view(request):
    return render(request,'deniedaccess/404.html')