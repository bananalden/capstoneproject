from django import forms
from .models import CustomUser
from .models import Student
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

class StudentCreationForm(UserCreationForm):
     class Meta:
        model = Student
        fields = ( 
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )