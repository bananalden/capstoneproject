from django.shortcuts import render, HttpResponse, redirect
from users import forms
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from transactions.models import PaymentPurpose
from transactions.forms import PaymentPurposeForm

# Create your views here.

@login_required(login_url='authentication:login')
def home(request):
    if request.user.role != "ADMIN":
        return redirect('authentication:unauthorized-view')
    return render(request, 'dashboard.html')


def payment_purpose_list(request):
    purpose_list = PaymentPurpose.objects.all()
    form = PaymentPurposeForm()
    context={
        'form':form,
        'purpose_list':purpose_list
    }
    return render(request, 'registrar-purpose-list.html', context)



@login_required(login_url='authentication:login')
def edit_admin_user(request):
    if request.user.role != "ADMIN":
        return redirect('authentication:unauthorized-view')
    edit_admin = forms.edit_admin(instance=request.user)
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

