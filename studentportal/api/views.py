import pandas as pd
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model
from users import models as user_data
from news import models as news_data
from grades.models import Grades
from transactions import models as transactions_data
from django.db.models import Q

# Create your views here.
app_name = "api"

#USER GRABBING START ================================

def get_userdata(request,pk):
    try:
        user = get_user_model().objects.get(pk=pk)

        if user:
            data = {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'username': user.username,
            }

    
        return JsonResponse(data)


    except:
        return(JsonResponse({'error':'User not found'}, status=404))

#USER GRABBING END =================================

#NEWS GRABBING START ===============================

def news_list(request):
    announcements = news_data.Announcement.objects.all().order_by("-created_on")
    
    announcement_data = [
        {
            "id": announcement.id,
            "title": announcement.title,
            "body": announcement.body,
            "created_on": announcement.created_on.strftime("%Y-%m-%d"),
            "modified_on": announcement.modified_on.strftime("%Y-%m-%d"),
            "author": f"{announcement.author.first_name} {announcement.author.last_name}",
            "formatted_date": announcement.created_on.strftime("%B %d, %Y %I:%M %p"), 
        }
        for announcement in announcements
    ]

    return JsonResponse(announcement_data, safe=False)

def get_news(request):
    page = request.GET.get("page", 1)  
    news_list = news_data.Announcement.objects.all().order_by("-created_on")

    paginator = Paginator(news_list, 5)  
    try:
        news_page = paginator.page(page)
    except:
        news_page = paginator.page(1)  


    data = [
        {
            "id": news.id,
            "title": news.title,
            "body": news.body,
            "formatted_date": news.created_on.strftime("%B %d, %Y %I:%M %p"), 
            "author": f"{news.author.first_name} {news.author.last_name}",
        }
        for news in news_page
    ]

    return JsonResponse({
        "news": data,
        "page": news_page.number,
        "total_pages": paginator.num_pages,
    })

def get_news_object(request,pk):
    news_list = news_data.Announcement.objects.get(pk=pk)

    data = {
        "id": news_list.id,
        "title": news_list.title,
        "body": news_list.body
    }

    return JsonResponse(data)
#NEWS GRABBING END ===========================================

#PAYMENT PURPOSE START =======================================



def get_payment_data(request,pk):
    transaction = transactions_data.Transaction.objects.get(pk=pk)

    data = {
        "student_name": f"{transaction.student.first_name} {transaction.student.last_name}",
        "date_time":transaction.date_time.strftime("%B %d, %Y %I:%M %p"),
        "student_usn":transaction.student.username,
        "payment_purpose":transaction.payment_purpose,
        "payment_proof":transaction.payment_proof.url if transaction.payment_proof else None,
        "registrar_status":transaction.registrar_status,
        "amount":transaction.amount,
    }

    return JsonResponse(data)


def cashier_transaction_data_unconfirmed(request):
    page = request.GET.get("page",1)
    search_query = request.GET.get("q","")
    filter_status = request.GET.get("filter","")
    transaction_list = transactions_data.Transaction.objects.all().order_by("-date_time").filter(is_confirmed=False)
    

    if search_query:
        transaction_list = transaction_list.filter(
            Q(student__first_name__icontains=search_query) |
            Q(student__last_name__icontains=search_query) |
            Q(student__username__icontains=search_query) 
        )

    if filter_status:
        transaction_list = transaction_list.filter(payment_purpose = filter_status)

    

    paginator = Paginator(transaction_list,10)
    try:
        transaction_page = paginator.page(page)
    except:
        transaction_page = paginator.page(1)
    data = [{
        "id":transaction.id,
        "student_name":f"{transaction.student.first_name} {transaction.student.last_name}",
        "student_username":transaction.student.username,
        "date_time":transaction.date_time.strftime("%B %d, %Y %I:%M %p"),
        "is_confirmed":transaction.is_confirmed,
        "payment_purpose":transaction.payment_purpose,
        "payment_purpose_other":transaction.payment_purpose_other,
        "amount":transaction.amount,

    }
    for transaction in transaction_page
    ]

    return JsonResponse({
        "transaction":data,
        "page":transaction_page.number,
        "total_pages":paginator.num_pages
    })



def cashier_transaction_data_confirmed(request):
    page = request.GET.get("page",1)
    search_query = request.GET.get("q","")
    filter_status = request.GET.get("filter","")
    transaction_list = transactions_data.Transaction.objects.all().order_by("-date_time").filter(is_confirmed=True)
    

    if search_query:
        transaction_list = transaction_list.filter(
            Q(student__first_name__icontains=search_query) |
            Q(student__last_name__icontains=search_query) |
            Q(student__username__icontains=search_query) 
        )

    if filter_status:
        transaction_list = transaction_list.filter(payment_purpose = filter_status)

    

    paginator = Paginator(transaction_list,10)
    try:
        transaction_page = paginator.page(page)
    except:
        transaction_page = paginator.page(1)
    data = [{
        "id":transaction.id,
        "student_name":f"{transaction.student.first_name} {transaction.student.last_name}",
        "student_username":transaction.student.username,
        "date_time":transaction.date_time.strftime("%B %d, %Y %I:%M %p"),
        "is_confirmed":transaction.is_confirmed,
        "payment_purpose":transaction.payment_purpose,
        "payment_purpose_other":transaction.payment_purpose_other,
        "amount":transaction.amount,

    }
    for transaction in transaction_page
    ]

    return JsonResponse({
        "transaction":data,
        "page":transaction_page.number,
        "total_pages":paginator.num_pages
    })


def export_transaction(request):
    month_year = request.GET.get("month")

    if not month_year:
        return HttpResponse("Month and year not inputted!", status=400)
    
    try:
        year, month = map(int, month_year.split("-")) 
    except:
        return HttpResponse("Invalid date format!", status = 400)
    
    transactions = transactions_data.Transaction.objects.filter(date_time__year=year, date_time__month=month, is_confirmed=True)

    data =[{
        "student_usn": trans.student.username,
        "student_name": f"{trans.student.first_name} {trans.student.last_name}",
        "payment_purpose":trans.payment_purpose,
        "payment_purpose_other": trans.payment_purpose_other,
        "amount": trans.amount,
        "date":trans.date_time.strftime("%Y-%m-%d")
                }
        for trans in transactions
    ]

    if not data:
        return HttpResponse("No transactions were found...", status=404)
    
    df = pd.DataFrame(data)

    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f'attachment; filename="transactions_{month_year}.xlsx"'

    with pd.ExcelWriter(response, engine="openpyxl") as writer:
        df.to_excel(writer, index=False,sheet_name="Transactions")
    return response






def registrar_doc_list(request):
   page = request.GET.get("page",1)
   search_query = request.GET.get("q","")
   filter_semester = request.GET.get("filter","")
   pending_transactions = transactions_data.Transaction.objects.filter(
        registrar_status__in=[
            transactions_data.Transaction.RegistrarStatus.PENDING,
            transactions_data.Transaction.RegistrarStatus.AVAILABLE,
            
            ],
        payment_purpose__in=[
            transactions_data.Transaction.PaymentPurposeChoice.CERT_GRADES,
            transactions_data.Transaction.PaymentPurposeChoice.CERT_MORALE,
            transactions_data.Transaction.PaymentPurposeChoice.CERT_ENROL
        ], is_confirmed=True
    ).order_by('-date_time')
   
   if filter_semester in ["1st","2nd"]:
       pending_transactions = pending_transactions.filter(semester=filter_semester)

   if search_query:
       pending_transactions = pending_transactions.filter(
            Q(student__first_name__icontains=search_query) |
            Q(student__last_name__icontains=search_query) |
            Q(student__username__icontains=search_query) 
       )
   
   paginator = Paginator(pending_transactions, 10)
   try:
       pend_trans_page = paginator.page(page)
   except:
       pend_trans_page = paginator.page(1)
    
   data = [{
       "id":pend_trans.id,
       "student_usn": pend_trans.student.username,
       "student_name":f"{pend_trans.student.first_name} {pend_trans.student.last_name}",
       "date_time": pend_trans.date_time.strftime("%B %d, %Y %I:%M %p"),
       "payment_purpose": pend_trans.payment_purpose,
       "registrar_status": pend_trans.registrar_status

    }
    for pend_trans in pend_trans_page
    ]
   return JsonResponse({
       "registrar_list": data,
       "page":pend_trans_page.number,
       "total_pages": paginator.num_pages
   })
   
       

def student_transaction_list(request):
    page = request.GET.get("page",1)
    filter_status = request.GET.get("filter","")
    transaction_list = transactions_data.Transaction.objects.order_by("-date_time").filter(student=request.user)
    
    if filter_status:
        transaction_list = transaction_list.filter(payment_purpose = filter_status)

    

    paginator = Paginator(transaction_list,10)
    try:
        transaction_page = paginator.page(page)
    except:
        transaction_page = paginator.page(1)
    data = [{
        "id":transaction.id,
        "student_name":f"{transaction.student.first_name} {transaction.student.last_name}",
        "student_username":transaction.student.username,
        "date_time":transaction.date_time.strftime("%B %d, %Y %I:%M %p"),
        "is_confirmed":transaction.is_confirmed,
        "payment_purpose":transaction.payment_purpose,
        "registrar_status":transaction.registrar_status,
        "payment_purpose_other":transaction.payment_purpose_other,
        "amount":transaction.amount,

    }
    for transaction in transaction_page
    ]

    return JsonResponse({
        "transaction":data,
        "page":transaction_page.number,
        "total_pages":paginator.num_pages
    })

#TRANSACTION END ========================

def get_grades(request):
    page = request.GET.get("page",1)
    search_query = request.GET.get("q","")
    semester = request.GET.get("filter","")
    grade_list = Grades.objects.all()
    

    if search_query:
        grade_list = grade_list.filter(
            Q(student_usn__icontains=search_query) |
            Q(subject_code__icontains=search_query) |
            Q(subject_name__icontains=search_query) 
        )

    if semester:
        grade_list = grade_list.filter(semester = semester)

    

    paginator = Paginator(grade_list,10)
    try:
        grade_page = paginator.page(page)
    except:
        grade_page = paginator.page(1)
    data = [{
       "id":grade.id,
       "student_usn":grade.student_usn,
       "subject_code":grade.subject_code,
       "subject_name":grade.subject_name,
       "year":grade.year,
       "semester":grade.semester,
       "grade_value":grade.grade_value,


    }
    for grade in grade_page
    ]

    return JsonResponse({
        "grade":data,
        "page":grade_page.number,
        "total_pages":paginator.num_pages
    })

def get_specific_grade(request,pk):
     try:
        grade = Grades.objects.get(id=pk)

        if grade:
            data = {
                "id":grade.id,
                "student_usn":grade.student_usn,
                "subject_code":grade.subject_code,
                "subject_name":grade.subject_name,
                "year":grade.year,
                "semester":grade.semester,
                "grade_value":grade.grade_value,         
            }
        return JsonResponse(data)

    
     except:
        return(JsonResponse({'error':'User not found'}, status=404))

 


#PAYMENT PURPOSE START