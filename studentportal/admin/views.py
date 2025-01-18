from django.shortcuts import render, HttpResponse, redirect
from users import forms as user_forms
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        if request.POST.get("user_type") == 'ADMIN':
            form = user_forms.add_admin(request.POST)
            if form.is_valid():
                admin = form.save(commit=False)
                admin.set_password(
                    form.cleaned_data["password"]
                )
                admin.save()
                messages.success(request,"Admin successfully created!")
                return redirect('admin:users:admin-list')
            else:
                messages.warning(request,form.errors)
                return redirect('admin:users:admin-list')
            
        elif request.POST.get("user_type") == 'REGISTRAR':
            form = user_forms.add_registrar(request.POST)
            if form.is_valid():
                registrar = form.save(commit=False)
                registrar.set_password(
                    form.cleaned_data['password']
                )
                registrar.save()
                messages.success(request,"Registrar successfully created!")
                return redirect("admin:users:registrar-list")
            else:
                messages.warning(request,form.errors)
                return redirect('admin:users:registrar-list')
            
        elif request.POST.get("user_type") == 'CASHIER':
            form = user_forms.add_cashier(request.POST)
            if form.is_valid():
                cashier = form.save(commit=False)
                cashier.set_passsword(
                    form.cleaned_data['password']
                )
                cashier.save()
                messages.success(request,"Cashier added successfully!")
                return redirect("admin:users:cashier-list")
            else:
                messages.warning(request,form.errors)
                return redirect("admin:users:cashier-list")
    else:
        return render(request, 'dashboard.html')

