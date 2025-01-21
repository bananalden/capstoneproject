from django.shortcuts import render, HttpResponse, redirect
from users import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.





@login_required(login_url='authentication:login')
def home(request):
    return render(request, 'dashboard.html')

@login_required(login_url='authentication:login')
def edit_admin_user(request):
    edit_admin = forms.edit_admin(instance=request.user)
    context = {'form': edit_admin}
    return render(request,'editadmin.html', context)

