from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'dashboard.html')

def create_course(request):
    return render(request, 'createcourse.html')

def create_semester(request):
    return render(request, 'createsemester.html')

def create_subject(request):
    return render(request, 'createsubject.html')

def create_admin(request):
    return render(request, 'createadmin.html')

def create_teacher(request):
    return render(request, 'createteacher.html')

def create_student(request):
    return render(request, 'createstudent.html')

def create_cashier(request):
    return render(request, 'createcashier.html')

def create_registrar(request):
    return render(request, 'createregistrar.html')