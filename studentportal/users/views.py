from django.shortcuts import render, redirect
from users import forms
from django.shortcuts import get_object_or_404
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
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = make_password(form.cleaned_data['password'])

            admin = CustomUser(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            admin.save()
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
        edit_id = request.POST['id']
        obj = get_object_or_404(CustomUser, id=edit_id)
        form = forms.add_admin(request.POST, instance=obj)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = make_password(form.cleaned_data['password'])
            
            admin = CustomUser.objects.get(id=edit_id)
            admin.first_name = first_name
            admin.last_name = last_name
            admin.email = email
            admin.username = username
            admin.password = password
            admin.save()

            return redirect('admin:users:admin-list')
        else:
            print(form.errors.as_data())

def delete_admin(request):
    pass

#ADMIN CRUD ACTION END

#CASHIER ACTION START
def create_cashier(request):
    return render(request, 'createcashier.html')
#CASHIER ACTION END

#REGISTRAR ACTION START
def create_registrar(request):
    return render(request, 'createregistrar.html')
#REGISTRAR ACTION END

#TEACHER ACTION START
def create_teacher(request):
    return render(request, 'createteacher.html')
#TEACHER ACTION END

#STUDENT ACTION START
def create_student(request):
    return render(request, 'createstudent.html')
#STUDENT ACTION END
