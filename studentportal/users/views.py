from django.shortcuts import render

# Create your views here.

#PLACE CRUD OPERATIONS HERE


#ADMIN CRUD ACTION START
def create_admin(request):
    return render(request, 'createadmin.html')

#ADMIN CRUD ACTION END

#CASHIER ACTION START
def create_cashier(request):
    return render(request, 'createcashier.html')
#CASHIER ACTION END

#REGISTRAR ACTION START
def create_registrar(request):
    return render(request, 'createregistrar.html')
#REGISTRAR ACTION END

#TEACHER ACTION START
def create_teacher(request):
    return render(request, 'createteacher.html')
#TEACHER ACTION END

#STUDENT ACTION START
def create_student(request):
    return render(request, 'createstudent.html')
#STUDENT ACTION END
