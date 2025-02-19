from django.shortcuts import render,redirect
from transactions.forms import PaymentPurposeForm
from transactions.models import PaymentPurpose

# Create your views here.

def create_payment_purpose(request):
    if request.method == 'POST':
        form = PaymentPurposeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('admin:payment-purpose-list')
        else:
            print(form.errors)
            return redirect('admin:payment-purpose-list')
        
def edit_payment_purpose(request):
    if request.method == 'POST':
        payment_id = request.POST.get("id", None)
        if not payment_id:
            print("ID NOT FOUND")
            return redirect('admin:payment-purpose-list')
        payment_object = PaymentPurpose.objects.get(id=payment_id)

        form = PaymentPurposeForm(request.POST, instance=payment_object)

        if form.is_valid():
            form.save()
            return redirect('admin:payment-purpose-list')
        else:
            print(form.errors)
            return redirect('admin:payment-purpose-list')
        

def delete_payment_purpose(request):
    if request.method == 'POST':
        payment_id = request.POST.get("delete_id")
        payment_object = PaymentPurpose.objects.get(id=payment_id)
        payment_object.delete()
        return redirect('admin:payment-purpose-list')
        
  
