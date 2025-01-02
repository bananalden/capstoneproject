from django import forms
from .models import CustomUser
from .models import Student, StudentProfile, Subject, Course
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction



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
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Student
        fields = ['first_name','last_name','username','email']


