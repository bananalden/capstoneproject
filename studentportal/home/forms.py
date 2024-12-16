from django import forms
from django.contrib.auth.forms import UserCreationForm
from.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class NewUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields="__all__"


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email
    
    



    def __init__(self, *args, **kwargs):
        super(NewUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': ''})