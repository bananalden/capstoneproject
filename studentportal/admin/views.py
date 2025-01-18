from django.shortcuts import render, HttpResponse, redirect
from users import forms as user_forms
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        if request.POST.get("user_type") == 'STUDENT':
            pass
            
        elif request.POST.get("user_type") == 'TEACHER':
            pass
        
        elif request.POST.get("user_type") == 'REGISTRAR':
            pass
            
        elif request.POST.get("user_type") == 'CASHIER':
            pass
    else:
        return render(request, 'dashboard.html')

