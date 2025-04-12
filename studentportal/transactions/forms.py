import re
from django import forms
from django.utils.html import strip_tags
from transactions.models import Transaction
from notifications.models import Notification
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings

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
        self.fields["payment_proof"].widget.attrs.update({
            "accept":"image/*"
        })
        self.fields["amount"].widget.attrs.update({
        "min": "1",
        "step": "0.01",
            })
       

    def clean_amount(self):
        amount = self.cleaned_data.get("amount")

        if amount is not None:
            if amount < 0:
                raise ValidationError("Amount cannot be negative")
            if amount < 1:
                raise ValidationError("Amount must be at least 1.00")
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
            "is_confirmed": forms.RadioSelect(choices=[(True, "Accept"), (False, "Decline")])
        }
    def save(self, commit=True):
        instance = super().save(commit=False)

        if instance.is_confirmed:
            subject = "Payment Update"
            message = f"Hello {instance.student.first_name} {instance.student.last_name}, \n\nThis email is here to inform you that your payment has been confirmed!\n\nIf your payment was for a document request, please wait for an email showing the pickup date."
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [instance.student.email]
            send_mail(subject,message,from_email,recipient_list)

            Notification.objects.create(
                recipient = instance.student,
                message = f"Your payment has been confirmed by the cashier! If this transaction was a document request, please wait for a notification or an email to arrive shortly."
            )


            if commit:
                instance.save()
            return instance


        else:
            subject = "Payment Update"
            message = f"Hello {instance.student.first_name} {instance.student.last_name}, \n\nWe regret to inform you that your payment was not confirmed. Please contact the cashier to resolve this issue."
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [instance.student.email]
            send_mail(subject,message,from_email,recipient_list)

            Notification.objects.create(
                recipient = instance.student,
                message = f"There was an error confirming your payment, please contact the cashier to resolve this issue."
            )
            if commit:
                instance.save()
                instance.delete()
        
            return None


#FORM VALIDATION FOR DOCUMENT GENERATION===========================
class GoodMoraleForm(forms.Form):
    student = forms.CharField(max_length=150,widget=forms.TextInput(attrs={
        "placeholder":"Input student's USN",
        "class":"generate-document-input",
        "id":"student-name"
    }))
    year = forms.CharField(max_length=150,widget=forms.TextInput(attrs={
        "placeholder":"Enter the school year (ex. 2024-2025)",
        "class":"generate-document-input",
        "id":"sy"
    }))
   
    semester = forms.ChoiceField(choices=[("1st", "1st Semester"),("2nd", "2nd Semester")], widget=forms.Select(attrs={
        "class":"generate-document-select"
    }))


    def clean_student(self):
        student_usn = self.cleaned_data.get("student")

        if not student_usn:
            raise ValidationError("This field is required")
        try:
            student = User.objects.get(username=student_usn)
            
            return student
        except User.DoesNotExist:  
            raise ValidationError("User does not exist. Please enter a valid Student username.")
        
    def clean_year(self):
        year = self.cleaned_data.get('year')

        if not isinstance(year, str):
            raise ValidationError("Year must be a string")
        
        if re.match(r"^\d{4}$", year):
            next_year = str(int(year) + 1)
            return f"{year} - {next_year}"
    
        if re.match(r"^\d{4}-\d{4}$", year):
            start, end = map(int, year.split("-"))
            if end != start + 1:
                raise ValidationError("School year must span exactly one year, e.g. '2024-2025'.")
            return year

        raise ValidationError("Invalid school year format. Use 'YYYY' or 'YYYY-YYYY'.")

class EnrollmentForm(forms.Form):
    student = forms.CharField(max_length=150,widget=forms.TextInput(attrs={
        "placeholder":"Input student's USN",
        "class":"generate-document-input",
        "id":"student-name"
    }))
    year = forms.CharField(max_length=150,widget=forms.TextInput(attrs={
        "placeholder":"Enter the school year (ex. 2024-2025)",
        "class":"generate-document-input",
        "id":"sy"
    }))
    
    semester = forms.ChoiceField(choices=[("1st", "1st Semester"),("2nd", "2nd Semester")], widget=forms.Select(attrs={
        "class":"generate-document-select"
    }))
    

    def clean_student(self):
        student_usn = self.cleaned_data.get("student")

        if not student_usn:
            raise ValidationError("This field is required")
        try:
            student = User.objects.get(username=student_usn)
            return student
        except User.DoesNotExist:  
            raise ValidationError("User does not exist. Please enter a valid Student username.")
        
    def clean_year(self):
        year = self.cleaned_data.get('year')

        if not isinstance(year, str):
            raise ValidationError("Year must be a string")
        
        if re.match(r"^\d{4}$", year):
            next_year = str(int(year) + 1)
            return f"{year} - {next_year}"
    
        if re.match(r"^\d{4}-\d{4}$", year):
            start, end = map(int, year.split("-"))
            if end != start + 1:
                raise ValidationError("School year must span exactly one year, e.g. '2024-2025'.")
            return year

        raise ValidationError("Invalid school year format. Use 'YYYY' or 'YYYY-YYYY'.")

class CertificateOfGrades(forms.Form):
    student = forms.CharField(max_length=150,widget=forms.TextInput(attrs={
        "placeholder":"Input student's USN",
        "class":"generate-document-input",
        "id":"student-name"
    }))
    year = forms.CharField(max_length=150,widget=forms.TextInput(attrs={
        "placeholder":"Enter the school year (ex. 2024-2025)",
        "class":"generate-document-input",
        "id":"sy"
    }))

    semester = forms.ChoiceField(choices=[("1st", "1st Semester"),("2nd", "2nd Semester")], widget=forms.Select(attrs={
        "class":"generate-document-select"
    }))



    def clean_student(self):
        student_usn = self.cleaned_data.get("student")

        if not student_usn:
            raise ValidationError("This field is required")
        try:
            student = User.objects.get(username=student_usn)
            return student
        except User.DoesNotExist:  
            raise ValidationError("User does not exist. Please enter a valid Student username.")
        
    def clean_year(self):
        year = self.cleaned_data.get('year')

        if not isinstance(year, str):
            raise ValidationError("Year must be a string")
        
        if re.match(r"^\d{4}$", year):
            next_year = str(int(year) + 1)
            return f"{year} - {next_year}"
    
        if re.match(r"^\d{4}-\d{4}$", year):
            start, end = map(int, year.split("-"))
            if end != start + 1:
                raise ValidationError("School year must span exactly one year, e.g. '2024-2025'.")
            return year

        raise ValidationError("Invalid school year format. Use 'YYYY' or 'YYYY-YYYY'.")


            
#FORM VALIDATION FOR DOCUMENT GENERATION===========================

   
class manualTransactionAdd(forms.ModelForm):

    student = forms.CharField(
        max_length=150,  
        widget=forms.TextInput(attrs={"placeholder": "Enter student USN",
                                      "id":"student_usn"})
    )
    class Meta:
        model = Transaction
        fields = ["student","payment_purpose", "payment_purpose_other", "amount"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        CHOICES = [("", "-----SELECT TRANSACTION PURPOSE-----")] + list(Transaction.PaymentPurposeChoice.choices)
        self.fields["payment_purpose"].choices = CHOICES
        self.fields["payment_purpose"].widget.attrs.update({"id": "transaction"})

    
    def clean_student(self):
        student_username = self.cleaned_data.get("student")

        if not student_username:
            raise ValidationError("This field is required.")

        try:
            user = User.objects.get(username=student_username)
            return user  
        except User.DoesNotExist:
            raise ValidationError("User does not exist. Please enter a valid Student username.")


    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.is_confirmed = True
        if isinstance(instance.student, str):
            try:
                instance.student = User.objects.get(username=instance.student)
            except User.DoesNotExist:
                raise ValueError("User does not exist!")

        print(f"Before saving: student type = {type(instance.student)}, value = {instance.student}")  # Debugging

        
        if commit:
            instance.save()
        return instance