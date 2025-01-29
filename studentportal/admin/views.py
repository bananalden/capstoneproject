from django.shortcuts import render, HttpResponse, redirect
from users import forms
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='authentication:login')
def home(request):
    return render(request, 'dashboard.html')

@login_required(login_url='authentication:login')
def edit_admin_user(request):
    edit_admin = forms.edit_admin(instance=request.user)
    context = {
        'form': edit_admin,
        'user':request.user}
    return render(request,'editadmin.html', context)

def edit_admin_password(request):
    form = forms.change_password(request.user)
    context={
        'form':form
    }
    return render(request, 'editadmin-password.html', context)

