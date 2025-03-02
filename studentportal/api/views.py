import pandas as pd
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model
from users import models as user_data
from news import models as news_data
from transactions import models as transactions_data
from django.db.models import Q

# Create your views here.
app_name = "api"

#USER GRABBING START

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

#USER GRABBING END

#NEWS GRABBING START

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


#NEWS GRABBING END

#PAYMENT PURPOSE START



def get_payment_data(request,pk):
    transaction = transactions_data.Transaction.objects.get(pk=pk)

    data = {
        "student_name": f"{transaction.student.first_name} {transaction.student.last_name}",
        "date_time":transaction.date_time.strftime("%B %d, %Y %I:%M %p"),
        "student_usn":transaction.student.username,
        "payment_purpose":transaction.payment_purpose,
        "payment_proof":transaction.payment_proof.url if transaction.payment_proof else None,
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





#PAYMENT PURPOSE START