from django.shortcuts import render,redirect
from transactions.forms import PaymentPurposeForm

# Create your views here.

def create_payment_purpose(request):
    if request.method == 'POST':
        form = PaymentPurposeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('admin:payment-purpose-list')