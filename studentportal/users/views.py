import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from users import forms
from users import models
from django.contrib.auth import get_user_model,update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

#PLACE CRUD OPERATIONS HERE

#EDIT ADMIN OPERATIONS#####################################
def edit_user(request):
    if request.method == 'POST':
        form = forms.edit_user(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            logged_user_role = request.user.role

            match logged_user_role:
                case 'ADMIN':
                    messages.success(request, "User details successfully edited!")
                    return redirect('admin:dashboard')
                
                case 'CASHIER':
                    messages.success(request, "User details successfully edited!")
                    return redirect('home:cashier-home')

                case 'REGISTRAR':
                    messages.success(request, "User details successfully edited!")
                    return redirect('home:registrar-dashboard')
                
                case 'TEACHER':
                    messages.success(request, "User details successfully edited!")
                    return redirect('home:teacher-home')
        else:
             logged_user_role = request.user.role
             match logged_user_role:
                case 'ADMIN':
                    messages.warning(request, form.errors)
                    return redirect('admin:dashboard')
                
                case 'CASHIER':
                    messages.warning(request, form.errors)
                    return redirect('home:cashier-home')

                case 'REGISTRAR':
                    messages.warning(request, form.errors)
                    return redirect('home:registrar-dashboard')
                 
                case 'TEACHER':
                    messages.warning(request, form.errors)
                    return redirect('home:teacher-home')

#EDIT ADMIN OPERATIONS#####################################
def admin_dashboard_action(request):
      if request.method == 'POST':
##################LOGIC FOR STUDENT########################################################
        if request.POST.get("user_type") == 'STUDENT':
            form = forms.add_student(request.POST)
            if form.is_valid():
                student = form.save()

                course = request.POST.get("course")
                models.StudentProfile.objects.update_or_create(
                    student=student,defaults={"course":course}
                ) 

                messages.success(request,"Student successfully created!")
                return redirect('admin:dashboard')
            else:
                messages.warning(request,form.errors)
                return redirect('admin:dashboard')
  #####################LOGIC FOR TEACHER##################################################          
        elif request.POST.get("user_type") == 'TEACHER':
            form = forms.add_teacher(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Teacher successfully created!")
                return redirect('admin:dashboard')
            else:
                messages.warning(request,form.errors)
                return redirect('admin:dashboard')
###########################LOGIC FOR REGISTRAR#########################################
        elif request.POST.get("user_type") == 'REGISTRAR':
            form = forms.add_registrar(request.POST)
            if form.is_valid():
               form.save()
               messages.success(request,'Registrar successfully created!')
               return redirect('admin:dashboard')
            else:
                messages.warning(request,form.errors)
                return redirect('admin:dashboard')

 ###########################LOGIC FOR CASHIER#########################################           
        elif request.POST.get("user_type") == 'CASHIER':
            form = forms.add_cashier(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Cashier successfully created!')
                return redirect('admin:dashboard')
            else:
                messages.warning(request,form.errors)
                return redirect('admin:dashboard')


#CASHIER ACTION START===================================================
@login_required(login_url='authentication:login')
def create_cashier(request):
    if request.user.role != "ADMIN":
        return redirect('authentication:unauthorized-view')
    form = forms.add_cashier()
    cashiers = models.CustomUser.objects.filter(role="CASHIER")

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
    if request.user.role != "ADMIN":
        return redirect('authentication:unauthorized-view')
    form = forms.add_registrar()
    registrars = models.CustomUser.objects.filter(role="REGISTRAR")
   
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
    if request.user.role != "ADMIN":
        return redirect('authentication:unauthorized-view')
    user_form = forms.add_teacher()
    teacher = get_user_model()
    teachers = teacher.objects.filter(role='TEACHER')
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
    if request.user.role != "ADMIN":
        return redirect('authentication:unauthorized-view')
    user_form = forms.add_student()
    student = get_user_model()
    students = student.objects.filter(role='STUDENT').select_related("student_id")
 
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



def student_profile_update(request):
    if request.method == "POST":
        u_form = forms.StudentUserUpdate(request.POST, instance=request.user)
        p_form = forms.StudentProfileUpdate(request.POST,instance=request.user.student_id)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,"Your profile has been modified!")
            return redirect('home:student-profile')
        else:
            messages.warning(request,"Invalid inputs in profile editing, pelase fix!")
            return redirect('home:student-profile')
        
#STUDENT ACTION END=============================================


#USER PASSWORD EDIT=============================================

def change_password_user(request):

    if request.method == 'POST':
        form = forms.change_password(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)

            logged_user_role = request.user.role

            match logged_user_role:
                case 'ADMIN':
                    messages.success(request, "Password has successfully been updated!")
                    return redirect('admin:dashboard')
                case 'STUDENT':
                    messages.success(request, "Password has successfully been updated!")
                    return redirect('home:student-home')

                case 'CASHIER':
                    messages.success(request, "Password has successfully been updated!")
                    return redirect('home:cashier-home')

                case 'REGISTRAR':
                    messages.success(request, "Password has successfully been updated!")
                    return redirect('home:registrar-dashboard')
                
                    
                    
            
            return redirect('authentication:login')
        else:
            print(form.errors)
            logged_user_role = request.user.role
            match logged_user_role:
                case 'ADMIN':
                    messages.warning(request, form.errors)
                    return redirect('admin:dashboard')
                case 'STUDENT':
                    messages.warning(request, form.errors)
                    return redirect('home:student-home')

                case 'CASHIER':
                    messages.warning(request, form.errors)
                    return redirect('home:cashier-home')

                case 'REGISTRAR':
                    messages.warning(request, form.errors)
                    return redirect('home:registrar-home')
            messages.error(request, form.errors)

#USER PASSWORD EDIT=============================================


#BULK CREATE STUDENT =====================

def bulk_register_student(request):
    if request.method == "POST" and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']
        valid_mime_types = [
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            'application/vnd.ms-excel'
        ]
        valid_extensions = ['.xls', '.xlsx']
        file_mime_type = excel_file.content_type
        file_name = excel_file.name

        if file_mime_type not in valid_mime_types or not any(file_name.endswith(ext) for ext in valid_extensions):
            messages.warning(request, "Invalid file type. Please upload a valid Excel file (.xls or .xlsx).")
            return redirect('home:create-student-profile')

        try:
            df = pd.read_excel(excel_file, dtype={'USN': str, 'Password': str})

            required_columns = ['USN', 'First Name', 'Last Name', 'Email', 'Password', 'Course']
            if not all(col in df.columns for col in required_columns):
                messages.error(request, 'Missing required columns')
                return redirect('home:create-student-profile')

            new_students = []
            student_course_mapping = {}  # Save course for each username
            existing_usernames = set(models.Student.objects.values_list('username', flat=True))

            for _, row in df.iterrows():
                raw_username = row.get('USN')
                if raw_username is None or str(raw_username).strip() in ["", "nan", "None"]:
                    continue

                username = str(raw_username).strip().split('.')[0]
                if username in existing_usernames:
                    continue  # Skip if already exists

                raw_password = row.get('Password')
                if raw_password is None or str(raw_password).strip() in ["", "nan", "None"]:
                    messages.warning(request, f"Skipping {username}: Missing password")
                    continue

                password = str(raw_password).strip()
                first_name = str(row.get('First Name', '')).strip()
                last_name = str(row.get('Last Name', '')).strip()
                email = str(row.get('Email', '')).strip()
                course = str(row.get('Course', '')).strip()

                if not first_name or not last_name or not email:
                    messages.warning(request, f"Skipping {username}: Missing required fields")
                    continue

                new_student = models.Student(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=make_password(password),
                    role= models.Student.Role.STUDENT
                )
                new_students.append(new_student)
                student_course_mapping[username] = course  # Save course separately

            with transaction.atomic():
                created_students = models.Student.objects.bulk_create(new_students)

                new_profiles = []
                for student in created_students:
                    course = student_course_mapping.get(student.username, '')
                    profile = models.StudentProfile(
                        student=student,
                        course=course
                    )
                    new_profiles.append(profile)

                models.StudentProfile.objects.bulk_create(new_profiles)

            if created_students:
                messages.success(request, f"Successfully added {len(created_students)} students!")
            else:
                messages.warning(request, "No new students were added.")

        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('home:create-student-profile')

        return redirect('home:create-student-profile')
    else:
        messages.error(request, "No file uploaded")
        return redirect('home:create-student-profile')

#BULK CREATE STUDENT =====================