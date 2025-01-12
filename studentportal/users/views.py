from django.shortcuts import render, redirect, get_object_or_404
from users import forms
from users.models import CustomUserManager, CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

# Create your views here.

#PLACE CRUD OPERATIONS HERE


#ADMIN CRUD ACTION START
def create_admin(request):
    form = forms.add_admin()
    admin = get_user_model()
    admins = admin.objects.filter(role='ADMIN')
    
    if request.method == 'POST':
        form = forms.add_admin(request.POST)
        if form.is_valid():
            admin_user = form.save(commit=False)
            admin_user.set_password(
                form.cleaned_data["password"]
            )
            admin_user.save()
           
            return redirect('admin:users:admin-list')
        else:
            print(form.errors.as_data())
    else:
        
        context = {'form':form,
                   'admins':admins
                   }
        return render(request, 'createadmin.html',context)
    
def update_admin(request):
       if request.method =='POST':
        admin_id = request.POST.get("id", None)
        if not admin_id:
            print("Coudn't find this admin")
            return redirect('admin:users:admin-list')
        admin_user = CustomUser.objects.get(id=admin_id)
        form = forms.add_admin(request.POST, instance=admin_user)
        if form.is_valid():
            admin_change = form.save(commit=False)
            admin_change.set_password(
                form.cleaned_data["password"]
                )
            admin_change.save()
            return redirect ('admin:users:admin-list')
        else:
            print(form.errors.as_data())
        
#ADMIN CRUD ACTION END

#CASHIER ACTION START
def create_cashier(request):
    form = forms.add_cashier()
    cashier = get_user_model()
    cashiers = cashier.objects.filter(role='CASHIER')
    
    if request.method == 'POST':
        form = forms.add_cashier(request.POST)
        if form.is_valid():
            cashier_user = form.save(commit=False)
            cashier_user.set_password(
                form.cleaned_data["password"]
            )
            cashier_user.save()
           
            return redirect('admin:users:cashier-list')
        else:
            print(form.errors.as_data())
    else:
        
        context = {'form':form,
                   'cashiers':cashiers
                   }
        return render(request, 'createcashier.html',context)

#CASHIER ACTION END

#REGISTRAR ACTION START
def create_registrar(request):
    form = forms.add_registrar()
    registrar = get_user_model()
    registrars = registrar.objects.filter(role='REGISTRAR')
    if request.method == 'POST':
        form = forms.add_registrar(request.POST)
        if form.is_valid():
            registrar_user = form.save(commit=False)
            registrar_user.set_password(
                    form.cleaned_data["password"]
                )
            
            registrar_user.save()
            return redirect('admin:users:registrar-list')
    else:
        context = {
            'form':form,
            'registrars':registrars
        }
        return render(request, 'createregistrar.html',context)
#REGISTRAR ACTION END

#TEACHER ACTION START
def create_teacher(request):
    return render(request, 'createteacher.html')
#TEACHER ACTION END

#STUDENT ACTION START
def create_student(request):
    return render(request, 'createstudent.html')
#STUDENT ACTION END
