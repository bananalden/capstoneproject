from django import forms
from users import models
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.hashers import make_password

class add_admin(forms.ModelForm):

    class Meta:
        model = models.CustomUser
        fields = ['first_name','last_name','email','username','password']
        widgets = {
            'password':forms.PasswordInput
        }


class add_cashier(forms.ModelForm):
    class Meta:
        model = models.Cashier
        fields = ['first_name','last_name','email','username','password']
        widgets = {
            'password':forms.PasswordInput
        }

class add_registrar(forms.ModelForm):
    class Meta:
        model = models.Registrar
        fields = ['first_name','last_name','email','username','password']
        widgets = {
            'password':forms.PasswordInput
        }
