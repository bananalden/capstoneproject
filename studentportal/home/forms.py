from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class GeneralUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ( 
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            'role'
        )