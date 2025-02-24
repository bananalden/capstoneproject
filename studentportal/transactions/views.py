from django.shortcuts import render,redirect
from transactions.forms import StudentPaymentForm,updatePayment
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
            
  