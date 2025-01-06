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