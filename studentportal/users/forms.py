from django import forms
from users import models
from django.utils.html import strip_tags
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
import re

User = get_user_model()

class edit_user(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            "class":"first_name",
            "placeholder":"Enter your first name"
                                                       })
        self.fields["last_name"].widget.attrs.update({
            "class":"last_name",
            "placeholder":"Enter your last name"
                                                      })
        self.fields["email"].widget.attrs.update({
            "class":"email",
            "placeholder":"Enter your email"})
        
        self.fields["username"].widget.attrs.update({
            "class":"username",
            "placeholder":"Enter your username"})
    class Meta:
        model = models.CustomUser
        fields = ['first_name','last_name','email','username']


class change_password(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget.attrs.update({
            "class":"old_password",
            "placeholder":"Enter your old password"
        })
        self.fields["new_password1"].widget.attrs.update({
            "class":"new_password1",
            "placeholder":"Enter your new password"
        })
        self.fields["new_password2"].widget.attrs.update({
            "class":"new_password1",
            "placeholder":"Confirm your new password"
        })
        

    class Meta:
        model = models.CustomUser
        fields = ['old_password','new_password1','new_password2']

#DASHBOARD FORMS START

class add_cashier(forms.ModelForm):
    class Meta:
        model = models.Cashier
        fields = ['first_name','last_name','email','username']
        widgets = {
            'password':forms.PasswordInput
        }
    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if re.search(r'\d',first_name):
            raise ValidationError("First or last name cannot contain numbers!")
        return first_name
        
    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if re.search(r'\d',last_name):
            raise ValidationError("First or last name cannot contain numbers!")
        return last_name
    
    def save(self, commit=True, password=None):
        cashier = super().save(commit=False)
        if password is None:
            raise ValueError("Password must be provided for user creation!")
        
        cashier.set_password(password)
        if commit:
            cashier.save()
        return cashier


class add_teacher(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = ['first_name','last_name','email','username']
        widgets = {
            'password':forms.PasswordInput
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if re.search(r'\d',first_name):
            raise ValidationError("First or last name cannot contain numbers!")
        return first_name
        
    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if re.search(r'\d',last_name):
            raise ValidationError("First or last name cannot contain numbers!")
        return last_name

    def save(self, commit=True, password=None):
        teacher = super().save(commit=False)
        if password is None:
            raise ValueError("Password must be provided for user creation!")
        
        teacher.set_password(password)
        if commit:
            teacher.save()
        return teacher


class add_registrar(forms.ModelForm):
    class Meta:
        model = models.Registrar
        fields = ['first_name','last_name','email','username']
        widgets = {
            'password':forms.PasswordInput
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if re.search(r'\d',first_name):
            raise ValidationError("First or last name cannot contain numbers!")
        return first_name
        
    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if re.search(r'\d',last_name):
            raise ValidationError("First or last name cannot contain numbers!")
        return last_name
        
    def save(self, commit=True, password=None):
        registrar = super().save(commit=False)
        if password is None:
            raise ValueError("Password must be provided for user creation!")
        
        registrar.set_password(password)
        if commit:
            registrar.save()
        return registrar

class add_student(forms.ModelForm):

    class Meta:
        model = models.Student
        fields = ['first_name','last_name','email','username']
        widgets = {
            'password':forms.PasswordInput
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if re.search(r'\d',first_name):
            raise ValidationError("First or last name cannot contain numbers!")
        return first_name
        
    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if re.search(r'\d',last_name):
            raise ValidationError("First or last name cannot contain numbers!")
        return last_name

    def save(self, commit=True, password=None):
        student = super().save(commit=False)
        if password is None:
            raise ValueError("Password must be provided for user creation!")
        
        student.set_password(password)
        if commit:
            student.save()
        return student
    
#DASHBOARD FORMS END


class FirstLoginPassword(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        

class StudentUserUpdate(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['email']

class StudentProfileUpdate(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),)
    address = forms.TextInput()
    class Meta:
        model = models.StudentProfile
        fields = ["date_of_birth","address","gender","address","contact_info"]


#ADMIN EDIT FORM


class edit_cashier(forms.ModelForm):
    class Meta:
        model = models.Cashier
        fields = ['first_name','last_name','email','username','password']
        widgets = {
            'password':forms.PasswordInput
        }
    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if re.search(r'\d',first_name):
            raise ValidationError("First or last name cannot contain numbers!")
        return first_name
        
    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if re.search(r'\d',last_name):
            raise ValidationError("First or last name cannot contain numbers!")
        return last_name
    
    def save(self, commit=True):
        cashier = super().save(commit=False)
        cashier.set_password(self.cleaned_data['password'])

        if self.instance.pk is None:
            cashier.is_active = False

        if commit:
            cashier.save()


class edit_teacher(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = ['first_name','last_name','email','username','password']
        widgets = {
            'password':forms.PasswordInput
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if re.search(r'\d',first_name):
            raise ValidationError("First or last name cannot contain numbers!")
        return first_name
        
    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if re.search(r'\d',last_name):
            raise ValidationError("First or last name cannot contain numbers!")
        return last_name

    def save(self, commit=True):
        teacher = super().save(commit=False)
        teacher.set_password(self.cleaned_data['password'])

        if self.instance.pk is None:
            teacher.is_active = False
        if commit:
            teacher.save()


class edit_registrar(forms.ModelForm):
    class Meta:
        model = models.Registrar
        fields = ['first_name','last_name','email','username','password']
        widgets = {
            'password':forms.PasswordInput
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if re.search(r'\d',first_name):
            raise ValidationError("First or last name cannot contain numbers!")
        return first_name
        
    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if re.search(r'\d',last_name):
            raise ValidationError("First or last name cannot contain numbers!")
        return last_name
        
    def save(self, commit=True):
        registrar = super().save(commit=False)
        registrar.set_password(self.cleaned_data['password'])

        if self.instance.pk is None:
            registrar.is_active = False

        if commit:
            registrar.save()




class edit_student(forms.ModelForm):

    class Meta:
        model = models.Student
        fields = ['first_name','last_name','email','username','password']
        widgets = {
            'password':forms.PasswordInput
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if re.search(r'\d',first_name):
            raise ValidationError("First or last name cannot contain numbers!")
        return first_name
        
    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if re.search(r'\d',last_name):
            raise ValidationError("First or last name cannot contain numbers!")
        return last_name

    def save(self, commit=True):
        student = super().save(commit=False)
        student.set_password(self.cleaned_data['password'])
        
        if self.instance.pk is None:
            student.is_active = False

        if commit:
            student.save()

        return student
        



