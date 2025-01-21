from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        logged_user_role = request.user.role
        if logged_user_role == 'ADMIN':
            return redirect('admin:dashboard')
        elif logged_user_role == 'STUDENT':
            pass
        elif logged_user_role == 'TEACHER':
            pass
        elif logged_user_role == 'CASHIER':
            pass
        elif logged_user_role == 'REGISTRAR':
            return redirect('home:registrar-home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if user.role == 'ADMIN':
                return redirect('admin:dashboard')
            elif user.role == 'STUDENT':
                pass
            elif user.role == 'TEACHER':
                pass
            elif user.role == 'REGISTRAR':
                return redirect('home:registrar-home')
            elif user.role == 'CASHIER':
                return redirect('home:cashier-home')
        else:
            messages.warning(request,'Invalid User credentials')
            return redirect('authentication:login')
    else:
        return render(request, 'login/login.html')

def logout_user(request):
    logout(request)
    return redirect('authentication:login')

def unauthorized_view(request):
    return render(request,'deniedaccess/401.html')

