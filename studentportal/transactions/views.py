import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render,redirect
from transactions.forms import StudentPaymentForm,updatePayment,manualTransactionAdd
from transactions.models import Transaction
from users.models import Student
from django.contrib import messages




def student_payment_request(request):
    if request.method == 'POST':
        form = StudentPaymentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(user=request.user)
            messages.success(request,"Payment request succesfully sent!")
            return redirect('home:student-request-form')
        else:
            
            messages.warning(request,form.errors)
            return redirect('home:student-request-form')
        
def confirm_payment(request):
    if request.method == 'POST':
        transaction_id = request.POST.get("trans_id")
        transaction_instance = Transaction.objects.get(id=transaction_id)
        form = updatePayment(request.POST, instance=transaction_instance)

        if form.is_valid():
            
            messages.success(request,"Payment request succesfully confirmed!")
            form.save()
            return redirect('home:unconfirmed-cashier-transactions')
        else:
           
            messages.warning(request,form.errors)
            return redirect('home:unconfirmed-cashier-transactions')
        
def manual_request(request):
    if request.method == "POST":
        form = manualTransactionAdd(request.POST)

        if form.is_valid():
            messages.success(request,"Payment request succesfully confirmed!")
            form.save()
            return redirect('home:cashier-home')
        else:
            print(form.errors)
            return redirect('home:cashier-home')
        

            
  