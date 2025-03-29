import pandas as pd
from weasyprint import HTML
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from news.models import Announcement
from transactions import forms, models
from users.forms import edit_user, change_password, StudentProfileUpdate, StudentUserUpdate
from users.models import CustomUser, Student
from grades.models import Grades

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
        registrar_status=models.Transaction.RegistrarStatus.COMPLETE,
        payment_purpose__in=[
            models.Transaction.PaymentPurposeChoice.CERT_GRADES,
            models.Transaction.PaymentPurposeChoice.CERT_MORALE,
            models.Transaction.PaymentPurposeChoice.CERT_ENROL
        ], is_confirmed=True
    ).count()

    pending_transaction_list = models.Transaction.objects.filter(
        registrar_status__in=[
            models.Transaction.RegistrarStatus.PENDING,
            models.Transaction.RegistrarStatus.AVAILABLE,
            ],
        payment_purpose__in=[
            models.Transaction.PaymentPurposeChoice.CERT_GRADES,
            models.Transaction.PaymentPurposeChoice.CERT_MORALE,
            models.Transaction.PaymentPurposeChoice.CERT_ENROL
        ], is_confirmed=True
    ).order_by('-date_time')[:5]

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
    if request.method == 'POST':
        document_type = request.POST.get('document_type')
        transaction_id = request.POST.get('transID')
        pickup_date = request.POST.get('pickup-date')

        if document_type == 'CERTIFICATE OF ENROLLMENT':
            form = forms.EnrollmentForm(request.POST)
            template_name = 'pdf_templates/certificate_of_enrollment.html'

        elif document_type == 'CERTIFICATE OF GOOD MORALE':
            form = forms.GoodMoraleForm(request.POST)
            template_name = 'pdf_templates/certificate_of_good_morale.html'

        elif document_type == 'CERTIFICATE OF GRADES':
            form = forms.CertificateOfGrades(request.POST)
            template_name = "pdf_templates/certificate_of_grades.html"

        if form.is_valid():
        
            student = form.cleaned_data.get("student")
            year = form.cleaned_data.get('year')
            semester = form.cleaned_data.get('semester')

            transaction = get_object_or_404(models.Transaction, id=transaction_id)
            transaction.registrar_status = models.Transaction.RegistrarStatus.AVAILABLE
            transaction.save()

            print(student)

            if document_type == 'CERTIFICATE OF GRADES':
                student_usn = str(student.username)
                grades = Grades.objects.filter(student_usn=student_usn,year=year,semester=semester)

                if not grades.exists():
                    messages.warning(request,'No grades were found for the given student')
                    return redirect('home:generate-document')
                
                context = {
                    'student': student,
                    'year': year,
                    'semester':semester,
                    'grades':grades
                }

            else:
                context={
                    'student':student,
                    'year':year,
                    'semester':semester
                }
        

            html_content = render_to_string(template_name,context)
            pdf_file = HTML(string=html_content).write_pdf()

            transaction = get_object_or_404(models.Transaction, id=transaction_id)

            if transaction.registrar_status == 'PENDING':
                transaction.registrar_status = models.Transaction.RegistrarStatus.AVAILABLE
                transaction.save()
            else:
                pass

            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{document_type}_{student.username}.pdf"'

            return response
        else:
            print(form.errors)
            return redirect('home:generate-document')

def gen_cert_success(request):
    return render(request, 'registrar/document-success.html')



#GENERATING CERTIFICATES ====================================