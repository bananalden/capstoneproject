import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from news.models import Announcement
from transactions import forms, models


# Create your views here.

#CASHIER VIEWS START =============================

def cashier_home(request):
    transactions = models.Transaction.objects.order_by("-date_time").filter(is_confirmed=True)[:6]
    unconfirmed_transactions = models.Transaction.objects.filter(is_confirmed=False).count()

    context = {
        'transactions': transactions,
        'unconfirmed_transactions':unconfirmed_transactions
    }
    return render(request, 'cashier/dashboard.html', context)

def unconfirmed_transaction_cashier(request):
    form = forms.updatePayment()
    context = {
        'form': form
    }
    return render(request, 'cashier/unconfirmed-transactions.html', context)


def confirmed_transaction_cashier(request):
    return render(request, 'cashier/confirmed-transaction.html')

#CASHIER VIEWS END =============================


#REGISTRAR VIEWS START=================================

def registrar_home(request):
    return render(request, 'registrar/registrar.html')

def registrar_dashboard(request):
    return render(request, 'registrar/registrar-dashboard.html')


#REGISTRAR VIEWS END  =================================

#STUDENT VIEWS START ==================================
def student_home(request):
    return render(request,'studentview/studentdashboard.html')

def student_profile(request):
    return render(request,'studentview/studentprofile.html')

def student_requestform(request):

    form = forms.StudentPaymentForm()
    context = {
        'form':form
    }
    return render(request,'studentview/studentrequestform.html',context)

def student_newsfeed(request):
    return render(request,'studentview/newsfeed.html')

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

#TEACHER VIEWS START   ==================================