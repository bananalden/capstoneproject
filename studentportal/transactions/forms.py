from django import forms
from django.utils.html import strip_tags
from transactions.models import Transaction

class StudentPaymentForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ["payment_purpose","payment_proof","amount","payment_purpose_other"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['payment_proof'].widget.attrs.update({
            "id": "paymentproof",
            "style":"display: none;",
            "onchange":"updateFileName()"
                                                          })
        CHOICES = [("", "-----SELECT TRANSACTION PURPOSE-----")] + list(Transaction.PaymentPurposeChoice.choices)
        self.fields["payment_purpose"].choices = CHOICES
        self.fields["payment_purpose"].widget.attrs.update({"id": "transaction"})

    def save(self,user, commit=True):
        instance = super().save(commit=False)
        instance.student = user
        if commit:
            instance.save()
        return instance


class updatePayment(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ["is_confirmed"]

   
class manualTransactionAdd(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["student", "payment_purpose"]