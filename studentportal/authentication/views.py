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


        
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)

            match user.role:
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
            messages.warning(request,'Invalid USN or Password, please try again!')
            return redirect('authentication:login')
    else:
       
        return render(request, 'login/login.html')

def logout_user(request):
    logout(request)
    return redirect('authentication:login')

def unauthorized_view(request):
    return render(request,'deniedaccess/401.html')

