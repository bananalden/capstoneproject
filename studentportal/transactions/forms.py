from django import forms
from django.utils.html import strip_tags
from transactions.models import Transaction
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

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

    def clean_amount(self):
        amount = self.cleaned_data.get("amount")

        if amount is not None:
            return round(amount,2)
        return amount
    
    def clean_payment_purpose_other(self):
        payment_purpose_other = self.cleaned_data.get("payment_purpose_other")

        if not payment_purpose_other:
            return None
        return payment_purpose_other

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
        widgets = {
            "is_confirmed": forms.RadioSelect(choices=[(True, "Yes"), (False, "No")])
        }




        

   
class manualTransactionAdd(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ["student", "payment_purpose", "payment_purpose_other", "amount"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        CHOICES = [("", "-----SELECT TRANSACTION PURPOSE-----")] + list(Transaction.PaymentPurposeChoice.choices)
        self.fields["payment_purpose"].choices = CHOICES
        self.fields["payment_purpose"].widget.attrs.update({"id": "transaction"})
        self.fields["student"].widget = forms.TextInput(attrs={"placeholder": "Enter student username"})
    def clean_student(self):
        student_username = self.cleaned_data.get("student")
        print("Oughh im cleaning your input")
        if not student_username:
            raise ValidationError("This field is required.")

        try:
            user = User.objects.get(username=student_username)
            print(f"User ID:{user.id}")
            return user  # This ensures the form returns a User instance instead of a string
        except User.DoesNotExist:

            raise ValidationError("User does not exist. Please enter a valid Student username.")


    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.is_confirmed = True
        print(f"Before saving: student type = {type(instance.student)}, value = {instance.student}")  # Debugging

        
        if commit:
            instance.save()
        return instance