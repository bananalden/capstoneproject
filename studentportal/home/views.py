import pandas as pd
from weasyprint import HTML
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from news.models import Announcement
from transactions import forms, models
from users.forms import edit_user, change_password, StudentProfileUpdate, StudentUserUpdate
from users.models import CustomUser, Student


# Create your views here.

#CASHIER VIEWS START =============================

@login_required(login_url='authentication:login')
def cashier_home(request):
    if request.user.role != 'CASHIER':
        return redirect('authentication:unauthorized-view')
    transactions = models.Transaction.objects.order_by("-date_time").filter(is_confirmed=True)[:6]
    unconfirmed_transactions = models.Transaction.objects.filter(is_confirmed=False).count()
    form = forms.manualTransactionAdd()

    context = {
        'transactions': transactions,
        'unconfirmed_transactions':unconfirmed_transactions,
        'form': form
    }
    return render(request, 'cashier/dashboard.html', context)

@login_required(login_url='authentication:login')
def unconfirmed_transaction_cashier(request):
    if request.user.role != 'CASHIER':
        return redirect('authentication:unauthorized-view')
    form = forms.updatePayment()
    context = {
        'form': form
    }
    return render(request, 'cashier/unconfirmed-transactions.html', context)


@login_required(login_url='authentication:login')
def confirmed_transaction_cashier(request):
    if request.user.role != 'CASHIER':
        return redirect('authentication:unauthorized-view')
    return render(request, 'cashier/confirmed-transaction.html')

@login_required(login_url='authentication:login')
def edit_cashier(request):
    if request.user.role != 'CASHIER':
        return redirect('authentication:unauthorized-view')
    form = edit_user(instance=request.user)
    context = {
        'form':form
    }
    return render(request,'cashier/edit-cashier.html',context)

def edit_cashier_password(request):
    form = change_password(request.user)
    context={
        'form':form
    }
    return render(request,'cashier/edit-cashier-password.html', context)

#CASHIER VIEWS END =============================


#REGISTRAR VIEWS START=================================

def registrar_home(request):
    return render(request, 'registrar/registrar.html')

def registrar_dashboard(request):
    total_students = Student.student.count()
    pending_transactions = models.Transaction.objects.filter(
        registrar_status=models.Transaction.RegistrarStatus.PENDING,
        payment_purpose__in=[
            models.Transaction.PaymentPurposeChoice.CERT_GRADES,
            models.Transaction.PaymentPurposeChoice.CERT_MORALE,
            models.Transaction.PaymentPurposeChoice.CERT_ENROL
        ], is_confirmed=True
    ).count()
    ready_transactions = models.Transaction.objects.filter(
        registrar_status=models.Transaction.RegistrarStatus.AVAILABLE,
        payment_purpose__in=[
            models.Transaction.PaymentPurposeChoice.CERT_GRADES,
            models.Transaction.PaymentPurposeChoice.CERT_MORALE,
            models.Transaction.PaymentPurposeChoice.CERT_ENROL
        ], is_confirmed=True
    ).count()

    pending_transaction_list = models.Transaction.objects.filter(
        registrar_status=models.Transaction.RegistrarStatus.PENDING,
        payment_purpose__in=[
            models.Transaction.PaymentPurposeChoice.CERT_GRADES,
            models.Transaction.PaymentPurposeChoice.CERT_MORALE,
            models.Transaction.PaymentPurposeChoice.CERT_ENROL
        ], is_confirmed=True
    )[:5]

    context = {
        'total_students': total_students,
        'pending_transactions':pending_transactions,
        'ready_transactions':ready_transactions,
        'transactions':pending_transaction_list 
    }
    
    return render(request, 'registrar/registrar-dashboard.html',context)

def registrar_document_request(request):
    return render(request, 'registrar/document-request.html')

def registrar_generate_document(request):
    return render(request, 'registrar/generate-document.html')

def registrar_grade_list(request):
    return render(request,'registrar/registrar-student-grades.html')





#REGISTRAR VIEWS END  =================================

#STUDENT VIEWS START ==================================
def student_home(request):
    return render(request,'studentview/studentdashboard.html')

def student_profile(request):
    u_form = StudentUserUpdate(instance=request.user)
    p_form = StudentProfileUpdate(instance=request.user.student_id)
    context = {
            'u_form': u_form,
            'p_form': p_form,
            
        }

    return render(request,'studentview/studentprofile.html',context)

def student_edit_password(request):
    form = change_password(request.user)
    context={
        'form':form
    }
    return render(request,'studentview/studentchangepassword.html', context)


def student_requestform(request):

    form = forms.StudentPaymentForm()
    context = {
        'form':form
    }
    return render(request,'studentview/studentrequestform.html',context)

def student_newsfeed(request):
    return render(request,'studentview/newsfeed.html')

def student_transaction(request):
    return render(request, 'studentview/transaction-history.html')

#STUDENT VIEWS END   ==================================

#TEACHER VIEWS START   ==================================

@login_required(login_url='authentication:login')
def teacher_home(request):
    
    return render(request,'teacherview/teacherdashboard.html')


@login_required(login_url='authentication:login')
def teacher_newsfeed(request):
    announcement_list = Announcement.objects.all()

    p = Paginator(Announcement.objects.all(), 5)
    page = request.GET.get('page')
    announcements = p.get_page(page)

    context = {
        'announcements': announcements,
        'announcement_list': announcement_list
    }
    return render(request,'teacherview/teachernewsfeed.html',context)

def edit_teacher(request):
    form = edit_user(instance=request.user)
    context = {
        'form':form
    }
    return render(request,'teacherview/edit-teacher.html',context)

def edit_teacher_password(request):
    form = change_password(request.user)
    context={
        'form':form
    }
    return render(request,'teacherview/teacher-password.html', context)

#TEACHER VIEWS START   ==================================


#GENERATING CERTIFICATES ====================================

def generate_cert(request):
    pass


#GENERATING CERTIFICATES ====================================