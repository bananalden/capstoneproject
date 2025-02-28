import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render,redirect
from transactions.forms import StudentPaymentForm,updatePayment,manualTransactionAdd
from transactions.models import Transaction

        
#ADMIN PAYMENT PURPOSE MANAGEMENT END

def student_payment_request(request):
    if request.method == 'POST':
        form = StudentPaymentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(user=request.user)
            return redirect('home:student-request-form')
        else:
            print(form.errors)
            return redirect('home:student-request-form')
        
def confirm_payment(request):
    if request.method == 'POST':
        transaction_id = request.POST.get("trans_id")
        transaction_instance = Transaction.objects.get(id=transaction_id)
        form = updatePayment(request.POST, instance=transaction_instance)

        if form.is_valid():
            print(transaction_id)
            form.save()
            return redirect('home:unconfirmed-cashier-transactions')
        else:
            print(form.errors)
            return redirect('home:unconfirmed-cashier-transactions')
        
def manual_request(request):
    if request.method == "POST":
        form = manualTransactionAdd(request.POST)

        if form.is_valid():
            try:
                transaction = form.save(commit=False)
                print(f"Student Type: {type(transaction.student)}")
                print(f"Student Value: {transaction.student}")

                transaction.save()
                return redirect("home:cashier-home")
            except ValueError as e:
                print(f"ValueError{e}")
                return redirect('home:cashier-home')
            
        else:
            print(form.errors)
            return redirect('home:cashier-home')
        

            
  