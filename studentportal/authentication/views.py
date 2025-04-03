from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        logged_user_role = request.user.role
        match logged_user_role:
            case "ADMIN":
                return redirect('admin:dashboard')
            case "STUDENT":
                return redirect("home:student-home")
            case "TEACHER":
                return redirect("home:teacher-home")
            case "CASHIER":
                return redirect("home:cashier-home")
            case "REGISTRAR":
                return redirect("home:registrar-home")
    else:
        return render(request, 'authlogin/login.html')

def login_regular_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

    
        if user is not None:
            
            if user.role == 'ADMIN':
                messages.warning(request,'Invalid USN or Password, please try again!')
                return redirect('authentication:login')
            login(request,user)

            match user.role:
                case "STUDENT":
                    return redirect("home:student-home")
                case "TEACHER":
                    return redirect("home:teacher-home")
                case "CASHIER":
                    return redirect("home:cashier-home")
                case "REGISTRAR":
                    return redirect("home:registrar-home")
      
        else:
            messages.warning(request,'Invalid USN or Password, please try again!')
            return redirect('authentication:login')

def login_admin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.role != "ADMIN":
                messages.warning(request,'Invalid USN or Password, please try again!')
                return redirect('admin:admin-login')
            else:
                login(request,user)
                return redirect('admin:dashboard')
        else:
            messages.warning(request,'Invalid USN or Password, please try again!')
            return redirect('admin:admin-login')

def logout_user(request):
    logout(request)
    return redirect('authentication:login')

def unauthorized_view(request):
    return render(request,'deniedaccess/401.html')

# EMAIL SENT
def email_sent(request):
    return render(request,'email-sent.html')

# SET NEW PASSWORD
def set_new_pass(request):
    return render(request,'set-new-pass.html')

# PASSWORD RESET SUCCESS
def pass_success(request):
    return render(request,'pass-success.html')

