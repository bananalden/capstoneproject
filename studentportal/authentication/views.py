from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib import messages
from users.forms import FirstLoginPassword
from django.urls import reverse
from axes.handlers.proxy import AxesProxyHandler
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        logged_user_role = request.user.role
        match logged_user_role:
            case "ADMIN":
                return redirect('admin:dashboard')
            case "STUDENT":
                return redirect("home:student-home")
            case "CASHIER":
                return redirect("home:cashier-home")
            case "REGISTRAR":
                return redirect("home:registrar-dashboard")
            case "TEACHER":
                    return redirect('home:teacher-home')

    else:
        return render(request, 'authlogin/login.html')

def login_regular_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if AxesProxyHandler.is_locked(request, credentials={'username': username}):
            messages.warning(request, 'Your account has been locked due to too many failed login attempts. Please try again later or contact support.')
            return redirect(reverse('authentication:login'))
    
        if user is not None:
            
            if user.role == 'ADMIN':
                messages.warning(request,'Invalid USN or Password, please try again!')
                return redirect('authentication:login')
            
            login(request,user)

            match user.role:
                case "TEACHER":
                    return redirect('home:teacher-home')

                case "STUDENT":
                    return redirect("home:student-home")
                case "CASHIER":
                    return redirect("home:cashier-home")
                case "REGISTRAR":
                    return redirect("home:registrar-dashboard")
      
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

def first_log_password(request):
    if not request.user.is_authenticated or request.user.is_active:
        return redirect('authentication:login')

    form = FirstLoginPassword(user=request.user, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, "You have now been succesfully verified!")

            match user.role:
                    case "TEACHER":
                        return redirect('home:teacher-home')
                    case "STUDENT":
                        return redirect("home:student-home")
                    case "CASHIER":
                        return redirect("home:cashier-home")
                    case "REGISTRAR":
                        return redirect("home:registrar-dashboard")
        else:
            messages.warning(request,form.errors)
            print(form.errors)

    return render(request, 'registration/first-log-pass.html',{'form':form})

#SECTION FOR FORGOTTEN PASSWORD DONT MESS WITH THIS

# EMAIL SENT
def email_sent(request):
    return render(request,'email-sent.html')

# SET NEW PASSWORD
def set_new_pass(request):
    return render(request,'set-new-pass.html')

# PASSWORD RESET SUCCESS
def pass_success(request):
    return render(request,'pass-success.html')


#SECTION FOR FORGOTTEN PASSWORD DONT MESS WITH THIS