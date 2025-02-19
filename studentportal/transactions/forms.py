from django import forms
from django.utils.html import strip_tags
from transactions.models import Transaction, PaymentPurpose

class StudentPaymentForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ["payment_purpose","payment_proof"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields["payment_purpose"].widget.attrs.update({
            "id": "transaction"
        })
        self.fields["payment_purpose"].queryset = PaymentPurpose.objects.all()
        self.fields["payment_purpose"].empty_label = "----SELECT TRANSACTION TYPE----"

class PaymentPurposeForm(forms.ModelForm):
    class Meta:
        model = PaymentPurpose
        fields = ["payment_purpose","payment_price"]

    def clean_payment_purpose(self):
        payment_purpose = self.cleaned_data.get("payment_purpose")

        if PaymentPurpose.objects.filter(payment_purpose=payment_purpose).exists():
            error_message = "Payment purpose already exists. Please enter a unique purpose"
            raise forms.ValidationError(strip_tags(error_message))
        
        return payment_purpose

