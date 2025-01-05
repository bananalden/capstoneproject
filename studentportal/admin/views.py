from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'dashboard.html')

def user_management(request):
    return render(request, 'usermanagement.html')