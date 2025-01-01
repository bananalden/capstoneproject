from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import GeneralUserCreationForm, StudentCreationForm

# Create your views here.

#LOGIN SECTION

def index(request):
    #FUNCTION TO CHECK IF THE USER IS LOGGED IN
    if request.user.is_authenticated:
        currentUserRole = request.user.role
        if currentUserRole == 'STUDENT':
            return redirect('studentdashboard')
        if currentUserRole =='ADMIN':
            return redirect('moderatorview')
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
                if user.role =='FACULTY':
                    return redirect('facultydashboard')
                if user.role == 'ADMIN':
                    return redirect('moderatorview')
            else:
                messages.error(request, 'Invalid credentials, please enter your USN and password correctly.')
                return redirect('login')

        else:
            return render(request, 'login/login.html')

#LOGIN SECTION END

def createuser(request):
    form = StudentCreationForm()
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors.as_data())



    context = {'form': form}
    return render(request, 'test_template/index.html', context)

#STUDENT VIEWS START


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
def studentformrequest(request):
    user = request.user
    firstname = user.first_name
    lastname = user.last_name
    context = {'firstname' : firstname,
               'lastname':  lastname}
    if user.role != 'STUDENT':
        return redirect('accessdenied')
    return render(request, 'studentside/formrequest.html', context)

@login_required(login_url='login')
def studenttransactionhistory(request):
    user = request.user
    firstname = user.first_name
    lastname = user.last_name
    context = {'firstname' : firstname,
               'lastname':  lastname}
    if user.role != 'STUDENT':
        return redirect('accessdenied')
    return render(request, 'studentside/transactionhistory.html', context)





#STUDENT VIEWS END

#MODERATOR/ADMIN VIEWS START
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

@login_required(login_url='login')
def moderatorstudentuser(request):
    user = request.user
    firstname = user.first_name
    lastname = user.last_name
    context = {'firstname' : firstname,
               'lastname':  lastname}
    if user.role != 'ADMIN':
        return redirect('accessdenied')
    return render(request, 'moderatorside/studentuser.html', context)

@login_required(login_url='login')
def moderatorfacultyuser(request):
    user = request.user
    firstname = user.first_name
    lastname = user.last_name
    context = {'firstname' : firstname,
               'lastname':  lastname}
    if user.role != 'ADMIN':
        return redirect('accessdenied')
    return render(request, 'moderatorside/facultyuser.html', context)

@login_required(login_url='login')
def moderatorcashieruser(request):
    user = request.user
    firstname = user.first_name
    lastname = user.last_name
    context = {'firstname' : firstname,
               'lastname':  lastname}
    if user.role != 'ADMIN':
        return redirect('accessdenied')
    return render(request, 'moderatorside/cashieruser.html', context)

#MODERATOR/ADMIN VIEWS END

#FACULTY VIEWS START
@login_required(login_url='login')
def facultyview(request):
    user = request.user
    if user.role != 'FACULTY':
        return redirect('accessdenied')
    return render(request, 'facultyside/dashboard.html')
#FACULTY VIEWS END


#REGISTRAR VIEWS START
def registrardashboard(request):
    return render(request, 'registrarside/dashboard.html')

def registrarformrequest(request):
    return render(request, 'registrarside/formrequestlist.html')


#REGISTRAR VIEWS END


def cashierrview(request):
    return render(request, 'cashier/index.html')



@login_required(login_url='login')
def accessdenied(request):
    return render(request, 'error/401.html')




def logout_user(request):
    logout(request)
    return redirect('login')