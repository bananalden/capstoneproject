from django import forms
from users import models
from course import models as course_models
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.hashers import make_password

class edit_admin(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({"class":"first_name",
                                                       "placeholder":"Enter your first name"
                                                       })
        self.fields["last_name"].widget.attrs.update({"class":"last_name",
                                                      "placeholder":"Enter your last name"
                                                      })
        self.fields["email"].widget.attrs.update({"class":"email",
                                                  "placeholder":"Enter your email"})
        self.fields["username"].widget.attrs.update({"class":"username",
                                                     "placeholder":"Enter your username"
                                                     })
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


class add_cashier(forms.ModelForm):
    class Meta:
        model = models.Cashier
        fields = ['first_name','last_name','email','username','password']
        widgets = {
            'password':forms.PasswordInput
        }
    def save(self, commit=True):
        cashier = super().save(commit=False)
        cashier.set_password(self.cleaned_data['password'])
        if commit:
            cashier.save()


class add_registrar(forms.ModelForm):
    class Meta:
        model = models.Registrar
        fields = ['first_name','last_name','email','username','password']
        widgets = {
            'password':forms.PasswordInput
        }
    def save(self, commit=True):
        registrar = super().save(commit=False)
        registrar.set_password(self.cleaned_data['password'])
        if commit:
            registrar.save()

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
    teacher = forms.ModelChoiceField(queryset=models.Teacher.objects.filter(role='TEACHER'))
    course = forms.ModelChoiceField(queryset=course_models.Course.objects.all())
    class Meta:
        model = models.Student
        fields = ['first_name','last_name','email','username','password']
        widgets = {
            'password':forms.PasswordInput
        }

    def __init__(self, *args, **kwargs):
        super(add_student, self).__init__(*args, **kwargs)
        self.fields['teacher'].label_from_instance = lambda obj: "%s" % (obj.get_full_name())

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
