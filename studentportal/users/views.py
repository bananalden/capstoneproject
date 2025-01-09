from django.shortcuts import render

# Create your views here.

#PLACE CRUD OPERATIONS HERE


#ADMIN CRUD ACTION START
def create_admin(request):
    return render(request, 'createadmin.html')

#ADMIN CRUD ACTION END

#CASHIER ACTION START
def create_cashier(request):
    pass
#CASHIER ACTION END

#REGISTRAR ACTION START
def create_registrar(request):
    pass
#REGISTRAR ACTION END

#TEACHER ACTION START
def create_teacher(request):
    pass
#TEACHER ACTION END

#STUDENT ACTION START
def create_student(request):
    pass
#STUDENT ACTION END
