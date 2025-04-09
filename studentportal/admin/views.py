from django.shortcuts import render, HttpResponse, redirect
from users import forms
from news.forms import edit_news
from news.models import Announcement
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


# Create your views here.
def admin_login(request):
    if request.user.is_authenticated:
        user_role = request.user.role
        if user_role == 'ADMIN':
            return redirect('admin:dashboard')
        else:
            return redirect('authentication:login')
    return render(request, 'login/login.html')

@login_required(login_url='authentication:login')
def home(request):
    if request.user.role != "ADMIN":
        return redirect('authentication:unauthorized-view')
    return render(request, 'dashboard.html')


@login_required(login_url='authentication:login')
def edit_admin_user(request):
    if request.user.role != "ADMIN":
        return redirect('authentication:unauthorized-view')
    edit_admin = forms.edit_user(instance=request.user)
    context = {
        'form': edit_admin,
        'user':request.user}
    return render(request,'editadmin.html', context)

@login_required(login_url='authentication:login')
def edit_admin_password(request):
    if request.user.role != "ADMIN":
        return redirect('authentication:unauthorized-view')
    form = forms.change_password(request.user)
    context={
        'form':form
    }
    return render(request, 'editadmin-password.html', context)

@login_required(login_url='authentication:login')
def admin_newsfeed(request):
    if request.user.role != "ADMIN":
        return redirect('authentication:unauthorized-view')
    return render(request,'newsfeed-edit.html')

def edit_news_item(request):
    if request.method == "POST":
        newsID = request.POST.get("newsID")
        announcement_instance = Announcement.objects.get(id=newsID)
        form = edit_news(request.POST, instance=announcement_instance)
        if form.is_valid():
            form.save()
            messages.success(request,'Edited news item')
            return redirect('admin:admin-newsfeed')
        else:
            messages.warning(request,form.errors)
            return redirect('admin:admin-newsfeed')
        
def delete_news_item(request):
    if request.method == "POST":
        newsID = request.POST.get("newsID")
        announcement_instance = Announcement.objects.get(id=newsID)
        announcement_instance.delete()
        messages.warning(request,'Announcement succesfully deleted')
        return redirect('admin:admin-newsfeed')