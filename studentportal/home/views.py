from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

#CASHIER VIEWS START =============================

def cashier_home(request):
    return render(request, 'cashier/dashboard.html')

def transaction_cashier(request):
    return render(request, 'cashier/transaction.html')

#CASHIER VIEWS END =============================


def registrar_home(request):
    return render(request, 'registrar/registrar.html')

def student_home(request):
    return render(request,'studentview/studentdashboard.html')