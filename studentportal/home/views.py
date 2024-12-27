from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import GeneralUserCreationForm, StudentCreationForm

# Create your views here.

def index(request):
    #FUNCTION TO CHECK IF THE USER IS LOGGED IN
    if request.user.is_authenticated:
        currentUserRole = request.user.role
        if currentUserRole == 'STUDENT':
            return redirect('studentdashboard')
        if currentUserRole =='ADMIN':
            return redirect('moderatordashboard')
    #REDIRECTS THEM DIRECTLY TO THE PROPER VIEW RATHER THAN A 401 
    else:  
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.role == 'STUDENT':
                    return redirect('studentdashboard')
                if user.role =='ADMIN':
                    return redirect('facultydashboard')
            else:
                messages.error(request, 'Invalid credentials, please enter your USN and password correctly.')
                return redirect('login')

        else:
            return render(request, 'login/login.html')

def createuser(request):
    form = StudentCreationForm()
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors.as_data())



    context = {'form': form}
    return render(request, 'test/usercreation.html', context)

@login_required(login_url='login')
def studentview(request):
    user = request.user
    firstname = user.first_name
    lastname = user.last_name
    context = {'firstname' : firstname,
               'lastname':  lastname}
    if user.role != 'STUDENT':
        return redirect('accessdenied')
    return render(request, 'studentside/dashboard.html', context)

@login_required(login_url='login')
def moderatorview(request):
    user = request.user
    firstname = user.first_name
    lastname = user.last_name
    context = {'firstname' : firstname,
               'lastname':  lastname}
    if user.role != 'ADMIN':
        return redirect('accessdenied')
    return render(request, 'moderatorside/dashboard.html', context)


def registrarview(request):
    return render(request, 'registrar/index.html')

def cashierrview(request):
    return render(request, 'cashier/index.html')

@login_required(login_url='login')
def facultyview(request):
    user = request.user
    if user.role != 'FACULTY':
        return redirect('accessdenied')
    return render(request, 'facultyside/dashboard.html')

@login_required(login_url='login')
def accessdenied(request):
    return render(request, 'error/401.html')

def sidebarview(request):
    return render(request, 'login/homepage.html')


def logout_user(request):
    logout(request)
    return redirect('login')