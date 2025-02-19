from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from news.models import Announcement
from transactions import forms


# Create your views here.

#CASHIER VIEWS START =============================

def cashier_home(request):
    return render(request, 'cashier/dashboard.html')
def transaction_cashier(request):
    return render(request, 'cashier/transaction.html')

#CASHIER VIEWS END =============================


#REGISTRAR VIEWS START=================================

def registrar_home(request):
    return render(request, 'registrar/registrar.html')

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