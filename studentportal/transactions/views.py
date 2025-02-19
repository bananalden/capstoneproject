from django.shortcuts import render,redirect
from transactions.forms import PaymentPurposeForm, StudentPaymentForm
from transactions.models import PaymentPurpose

# Create your views here.
#ADMIN PAYMENT PURPOSE MANAGEMENT START
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
            
  
