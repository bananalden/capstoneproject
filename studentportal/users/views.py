from django.shortcuts import render, redirect, get_object_or_404
from users import forms
from users import models
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

#PLACE CRUD OPERATIONS HERE

#EDIT ADMIN OPERATIONS#####################################
def edit_admin(request):
    if request.method == 'POST':
        form = forms.edit_admin(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('admin:edit-admin')
        else:
            messages.warning(request,"Invalid inputs!")
            return redirect('admin:edit-admin')
#EDIT ADMIN OPERATIONS#####################################
def admin_dashboard_action(request):
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


#CASHIER ACTION START===================================================
@login_required(login_url='authentication:login')
def create_cashier(request):
    form = forms.add_cashier()
    cashiers = models.CustomUser.objects.filter(role="CASHIER")
    
    if request.method == 'POST':
        form = forms.add_cashier(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Cashier successfully saved!')
            return redirect('admin:users:cashier-list')
        else:
            messages.warning(request,form.errors)
            return redirect('admin:users:cashier-list')
    else:
        
        context = {'form':form,
                   'cashiers':cashiers
                   }
        return render(request, 'createcashier.html',context)
    
def update_cashier(request):
    if request.method == 'POST':
        cashier_id = request.POST.get("id", None)
        if not cashier_id:
            print("Coudn't find this admin")
            return redirect('admin:users:admin-list')
        cashier_user = models.CustomUser.objects.get(id=cashier_id)
        form = forms.add_cashier(request.POST, instance=cashier_user)
        if form.is_valid():
            form.save()
            messages.success(request,"Cashier successfully edited!")
            return redirect ('admin:users:cashier-list')
        else:
            messages.warning(request,form.errors)
            return redirect ('admin:users:cashier-list')
def delete_cashier(request):
    if request.method == "POST":
        cashier_id = request.POST['delete_id']
        cashier_user = models.CustomUser.objects.get(id=cashier_id)
        cashier_user.delete() 
        messages.warning(request,"Cashier successfully deleted")
        return redirect("admin:users:cashier-list") 

#CASHIER ACTION END============================================

#REGISTRAR ACTION START========================================
@login_required(login_url='authentication:login')
def create_registrar(request):
    form = forms.add_registrar()
    registrars = models.CustomUser.objects.filter(role="REGISTRAR")
    if request.method == 'POST':
        form = forms.add_registrar(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registrar successfully added!')
            return redirect('admin:users:registrar-list')
        else:
            messages.warning(request,form.errors)
            return redirect('admin:users:registrar-list')
    else:
        context = {
            'form':form,
            'registrars':registrars
        }
        return render(request, 'createregistrar.html',context)
    

def update_registrar(request):
    if request.method == 'POST':
        registrar_id = request.POST.get("id", None)
        registrar_user = models.CustomUser.objects.get(id=registrar_id)
        form = forms.add_registrar(request.POST, instance=registrar_user)
        if form.is_valid():
            form.save()
            messages.success(request,"Registrar has been successfully edited!")
            return redirect ('admin:users:registrar-list')
        else:
            messages.warning(request, form.errors)
            return redirect ('admin:users:registrar-list')

def delete_registrar(request):
    if request.method == "POST":
        registrar_id = request.POST['delete_id']
        registrar_user = models.CustomUser.objects.get(id=registrar_id)
        registrar_user.delete()
        messages.warning(request,"Registrar successfully deleted") 
        return redirect("admin:users:registrar-list")

#REGISTRAR ACTION END==============================================

#TEACHER ACTION START==============================================
@login_required(login_url='authentication:login')
def create_teacher(request):
    user_form = forms.add_teacher()
    teacher = get_user_model()
    teachers = teacher.objects.filter(role='TEACHER').select_related("teacher_id")
    if request.method == 'POST':
        user_form = forms.add_teacher(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request,"Teacher added successfully!")
            return redirect('admin:users:teacher-list')
        else:
            messages.warning(request,user_form.errors)
            return redirect('admin:users:teacher-list')
            
    else:
        context = {'user_form':user_form,
                   'teachers':teachers
                }
        return render(request, 'createteacher.html',context)
    
def update_teacher(request):
    if request.method == 'POST':
        teacher_id = request.POST.get("edit_id")
        teacher_user = models.CustomUser.objects.get(id=teacher_id)
        teacher_update =forms.add_teacher(request.POST, instance=teacher_user)
        if teacher_update.is_valid():
            teacher_update.save()
            messages.success(request,'Teacher updated successfully!')
            return redirect('admin:users:teacher-list')
        else:
            messages.warning(request,teacher_update.errors)
            return redirect('admin:users:teacher-list')


def delete_teacher(request):
    if request.method == 'POST':
        teacher_id = request.POST.get("delete_id")
        teacher_user = models.CustomUser.objects.get(id=teacher_id)
        teacher_user.delete()
        messages.warning(request,'Teacher deleted successfully')
        return redirect('admin:users:teacher-list')

#TEACHER ACTION END=================================================

#STUDENT ACTION START===============================================
@login_required(login_url='authentication:login')
def create_student(request):
    user_form = forms.add_student()
    student = get_user_model()
    students = student.objects.filter(role='STUDENT').select_related("student_id")
    if request.method == 'POST':
        user_form = forms.add_student(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request,'Student added successfully!')
            return redirect('admin:users:student-list')
        else:
            messages.warning(request,user_form.errors)
            return redirect('admin:users:student-list')
            
    else:
        context = {'user_form':user_form,
                   'students':students
                }
        return render(request, 'createstudent.html',context)
    
def update_student(request):
    if request.method == 'POST':
        student_id = request.POST.get("edit_id")
        student_user = models.CustomUser.objects.get(id=student_id)
        student_update =forms.add_student(request.POST, instance=student_user)
        if student_update.is_valid():
            student_update.save()
            messages.success(request,"Student edited successfully!")
            return redirect('admin:users:student-list')
        else:
            messages.warning(request,student_update.errors)
            return redirect('admin:users:student-list')

def delete_student(request):
     if request.method == 'POST':
        student_id = request.POST.get("delete_id")
        student_user = models.CustomUser.objects.get(id=student_id)
        student_user.delete()
        messages.warning(request,"Student deleted successfully")
        return redirect('admin:users:student-list')

#STUDENT ACTION END=============================================
