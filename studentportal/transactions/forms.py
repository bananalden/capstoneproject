from django.forms import ModelForm
from transactions.models import Transaction, PaymentPurpose

class StudentPaymentForm(ModelForm):

    class Meta:
        model = Transaction
        fields = ["payment_purpose","payment_proof"]

class PaymentPurposeForm(ModelForm):
    class Meta:
        model = PaymentPurpose
        fields = ["payment_purpose","payment_price"]

