from django import forms
from django.contrib.auth.forms import UserCreationForm
from users import models

class add_admin(forms.ModelForm):
    class Meta:
        model = models.CustomUser
        fields = ['first_name','last_name','email','username','password']
        widgets = {
            'password':forms.PasswordInput
        }