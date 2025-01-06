from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'dashboard.html')

def create_admin(request):
    return render(request, 'createadmin.html')

def create_teacher(request):
    return render(request, 'createteacher.html')

def create_cashier(request):
    return render(request, 'createcashier.html')

def create_student(request):
    return render(request, 'createstudent.html')

def create_registrar(request):
    return render(request, 'createregistrar.html')
