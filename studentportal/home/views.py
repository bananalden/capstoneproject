import pandas as pd
import datetime
from weasyprint import HTML
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
from news.models import Announcement
from transactions import forms, models
from users.forms import edit_user, change_password, StudentProfileUpdate, StudentUserUpdate
from users.models import CustomUser, Student
from notifications.models import Notification
from grades.models import Grades
from django.core.mail import send_mail
from django.conf import settings

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
    if request.user.role != 'CASHIER':
        return redirect('authentication:unauthorized-view')
    form = change_password(request.user)
    context={
        'form':form
    }
    return render(request,'cashier/edit-cashier-password.html', context)

#CASHIER VIEWS END =============================


#REGISTRAR VIEWS START=================================

@login_required(login_url='authentication:login')
def registrar_home(request):
    if request.user.role != 'REGISTRAR':
        return redirect('authentication:unauthorized-view')
    return render(request, 'registrar/registrar.html')

@login_required(login_url='authentication:login')
def registrar_dashboard(request):
    if request.user.role != 'REGISTRAR':
        return redirect('authentication:unauthorized-view')
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

@login_required(login_url='authentication:login')
def edit_registrar(request):
    if request.user.role != 'REGISTRAR':
        return redirect('authentication:unauthorized-view')
    form = edit_user(instance=request.user)
    context = {
        'form':form
    }
    return render(request,'registrar/edit-registrar.html',context)

@login_required(login_url='authentication:login')
def edit_registrar_password(request):
    if request.user.role != 'REGISTRAR':
        return redirect('authentication:unauthorized-view')
    form = change_password(request.user)
    context={
        'form':form
    }
    return render(request,'registrar/edit-registrar-password.html', context)

@login_required(login_url='authentication:login')
def registrar_document_request(request):
    if request.user.role != 'REGISTRAR':
        return redirect('authentication:unauthorized-view')
    if request.GET.get("success") == "1":
        messages.success(request, "Certificate has been successfully downloaded.")
    return render(request, 'registrar/document-request.html')

@login_required(login_url='authentication:login')
def registrar_document_complete(request):
    if request.user.role != 'REGISTRAR':
        return redirect('authentication:unauthorized-view')
    return render(request, 'registrar/document-list-complete.html')

@login_required(login_url='authentication:login')
def registrar_generate_document(request):
    if request.GET.get("success") == "1":
        messages.success(request, "Certificate has been successfully downloaded.")

    if request.user.role != 'REGISTRAR':
        return redirect('authentication:unauthorized-view')
    return render(request, 'registrar/generate-document.html')

@login_required(login_url='authentication:login')
def registrar_create_student(request):
    if request.user.role != 'REGISTRAR':
        return redirect('authentication:unauthorized-view')
    return render(request,'registrar/create-student-profile.html')

@login_required(login_url='authentication:login')
def registrar_grade_list(request):
    if request.user.role != 'REGISTRAR':
        return redirect('authentication:unauthorized-view')
    return render(request,'registrar/registrar-student-grades.html')


@login_required(login_url='authentication:login')
def registrar_upload_grades(request):
    if request.user.role != 'REGISTRAR':
        return redirect('authentication:unauthorized-view')
    
    return render(request,'registrar/registrar-upload-grades.html')





#REGISTRAR VIEWS END  =================================

#STUDENT VIEWS START ==================================
@login_required(login_url='authentication:login')
def student_home(request):
    if request.user.role != 'STUDENT':
        return redirect('authentication:unauthorized-view')
    return render(request,'studentview/studentdashboard.html')

@login_required(login_url='authentication:login')
def student_profile(request):
    if request.user.role != 'STUDENT':
        return redirect('authentication:unauthorized-view')
    u_form = StudentUserUpdate(instance=request.user)
    p_form = StudentProfileUpdate(instance=request.user.student_id)
    context = {
            'u_form': u_form,
            'p_form': p_form,
            
        }

    return render(request,'studentview/studentprofile.html',context)

@login_required(login_url='authentication:login')
def student_edit_password(request):
    if request.user.role != 'STUDENT':
        return redirect('authentication:unauthorized-view')
    form = change_password(request.user)
    context={
        'form':form
    }
    return render(request,'studentview/studentchangepassword.html', context)


@login_required(login_url='authentication:login')
def student_requestform(request):
    if request.user.role != 'STUDENT':
        return redirect('authentication:unauthorized-view')
    form = forms.StudentPaymentForm()
    context = {
        'form':form
    }
    return render(request,'studentview/studentrequestform.html',context)

@login_required(login_url='authentication:login')
def student_newsfeed(request):
    if request.user.role != 'STUDENT':
        return redirect('authentication:unauthorized-view')
    return render(request,'studentview/newsfeed.html')

@login_required(login_url='authentication:login')
def student_transaction(request):
    if request.user.role != 'STUDENT':
        return redirect('authentication:unauthorized-view')
    return render(request, 'studentview/transaction-history.html')

#STUDENT VIEWS END   ==================================

#TEACHER VIEWS START   ==================================




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

        elif document_type == "TRANSCRIPT OF RECORDS":
            form = forms.TranscriptRecords(request.POST)
            template_name = "pdf_templates/transcript_records.html"

        if form.is_valid():        
            student = form.cleaned_data.get("student")
            year = form.cleaned_data.get('year')
            semester = form.cleaned_data.get('semester')
            transaction = get_object_or_404(models.Transaction, id=transaction_id)

            if document_type == 'CERTIFICATE OF GRADES':
                student_usn = str(student.username)
                grades = Grades.objects.filter(student_usn=student_usn,year=year,semester=semester)

                if not grades.exists():
                    return JsonResponse({
                        "status":"error",
                        "message":"No grades found for this student"
                    },status=400)
                
                context = {
                    'student': student,
                    'year': year,
                    'semester':semester,
                    'grades':grades
                }
            
            elif document_type =="TRANSCRIPT OF RECORDS":
                student_usn = str(student.username)
                grades_unfiltered = Grades.objects.filter(student_usn=student_usn)
                grades = grades_unfiltered.sort(key=lambda g: (g.sort_year, g.sort_semester))

            else:
                context={
                    'student':student,
                    'year':year,
                    'semester':semester
                }
        

            html_content = render_to_string(template_name,context)
            pdf_file = HTML(string=html_content).write_pdf()

           
            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{document_type}_{student.username}.pdf"'

            if transaction.registrar_status != models.Transaction.RegistrarStatus.AVAILABLE:
                if not pickup_date:
                    return JsonResponse({
                "status":"error",
                "message":"Pick up date is required"
            },status=400)
                
                transaction.registrar_status = models.Transaction.RegistrarStatus.AVAILABLE
                transaction.save()

                #CONVERT THE DATE INTO ANOTHER FORMAT
                pickup_date_obj = datetime.datetime.strptime(pickup_date, "%Y-%m-%d")  
                formatted_datetime = pickup_date_obj.strftime("%B %d, %Y")

                Notification.objects.create(
                    title="REGISTRAR UPDATE",
                    recipient=transaction.student,
                    message = f"Your request for {transaction.payment_purpose} has been generated! Please receive by {formatted_datetime}"
                )

                subject = "Document Request Update"
                message = f"Hello {transaction.student.first_name} {transaction.student.last_name}, \n\nThis email is here to inform you that your request for {transaction.payment_purpose} is now available for pickup! \n\n Please pick up by {formatted_datetime}."
                from_email = settings.DEFAULT_FROM_EMAIL
                recipient_list = [transaction.student.email]
                send_mail(subject,message,from_email,recipient_list)
            


            return response
        else:
            print(form.errors)
            return JsonResponse({
                        "status":"error",
                        "message":"Invalid form data",
                        "errors":form.errors
                    },status=400)

def gen_cert_success(request):
    return render(request, 'registrar/document-success.html')



#GENERATING CERTIFICATES ====================================