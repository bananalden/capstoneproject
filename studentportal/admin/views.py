from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'dashboard.html')

def create_course(request):
    return render(request, 'createcourse.html')