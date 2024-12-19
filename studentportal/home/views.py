from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import GeneralUserCreationForm, StudentCreationForm

# Create your views here.



def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'STUDENT':
                return redirect('studentview')
            if user.role =='ADMIN':
                return redirect('facultyview')
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
    #user = request.user
   # if user is not user.role == 'STUDENT':
        #return redirect('')

        return render(request, 'studentside/index.html')

def registrarview(request):
    return render(request, 'registrar/index.html')

def cashierrview(request):
    return render(request, 'cashier/index.html')

@login_required(login_url='login')
def facultyview(request):
    return render(request, 'faculty/index.html')

def logout_user(request):
    logout(request)
    return redirect('login')