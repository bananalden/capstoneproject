from django.shortcuts import render, HttpResponse, redirect
from users import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.





@login_required(login_url='authentication:login')
def home(request):
    if request.method == 'POST':
##################LOGIC FOR STUDENT########################################################
        if request.POST.get("user_type") == 'STUDENT':
            form = forms.add_student(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Student successfully created!")
                return redirect('admin:users:student-list')
            else:
                messages.warning(request,form.errors)
                return redirect('admin:users:student-list')
  #####################LOGIC FOR TEACHER##################################################          
        elif request.POST.get("user_type") == 'TEACHER':
            form = forms.add_teacher(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Teacher successfully created!")
                return redirect('admin:users:teacher-list')
            else:
                messages.warning(request,form.errors)
                return redirect('admin:users:teacher-list')
###########################LOGIC FOR REGISTRAR#########################################
        elif request.POST.get("user_type") == 'REGISTRAR':
            form = forms.add_registrar(request.POST)
            if form.is_valid():
               form.save()
               messages.success(request,'Registrar successfully created!')
               return redirect('admin:users:registrar-list')
            else:
                messages.warning(request,form.errors)
                return redirect('admin:users:registrar-list')

 ###########################LOGIC FOR CASHIER#########################################           
        elif request.POST.get("user_type") == 'CASHIER':
            form = forms.add_cashier(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Cashier successfully created!')
                return redirect('admin:users:cashier-list')
            else:
                messages.warning(request,form.errors)
                return redirect('admin:users:cashier-list')
    else:
        return render(request, 'dashboard.html')

#EDIT ADMIN USER START==================================================
@login_required(login_url='authentication:login')
def edit_admin_user(request):
    edit_admin = forms.edit_admin(instance=request.user)
    context = {'form': edit_admin}
    return render(request,'editadmin.html', context)
#EDIT ADMIN USER END====================================================
