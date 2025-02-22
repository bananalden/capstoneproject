from django.shortcuts import render,redirect
from transactions.forms import StudentPaymentForm

        
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
            
  