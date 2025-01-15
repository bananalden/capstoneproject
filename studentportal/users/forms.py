from django import forms
from users import models
from course import models as course_models
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

class add_teacher(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=course_models.Course.objects.all())
    class Meta:
        model = models.Teacher
        fields = ['first_name','last_name','email','username','password']
        widgets = {
            'password':forms.PasswordInput
        }
    
    def save(self, commit=True):
        teacher = super().save(commit=False)
        teacher.set_password(self.cleaned_data['password'])

        teacher.profile_data ={
            'course': self.cleaned_data.get('course')
        }

        if commit:
            teacher.save()

            profile, created = models.TeacherProfile.objects.get_or_create(teacher=teacher)
            profile.course = self.cleaned_data.get('course')
            profile.save()

        return teacher


class add_student(forms.ModelForm):
    teacher = forms.ModelChoiceField(queryset=models.Teacher.objects.all())
    course = forms.ModelChoiceField(queryset=course_models.Course.objects.all())
    class Meta:
        model = models.Student
        fields = ['first_name','last_name','email','username','password']
        widgets = {
            'password':forms.PasswordInput
        }
    
    def save(self, commit=True):
        student = super().save(commit=False)
        student.set_password(self.cleaned_data['password'])

        student.profile_data ={
            'course': self.cleaned_data.get('course'),
            'teacher':self.cleaned_data.get('teacher')
        }

        if commit:
            student.save()

            profile, created = models.StudentProfile.objects.get_or_create(student=student)
            profile.course = self.cleaned_data.get('course')
            profile.teacher = self.cleaned_data.get('teacher')
            profile.save()

        return student
