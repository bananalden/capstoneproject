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

class StudentCreationForm(forms.ModelForm):
    # Add fields from StudentProfile
    course = forms.ModelChoiceField(queryset=Course.objects.all(), required=True)
    enrolled_subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Student
        fields = ['first_name','last_name','username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()

    @transaction.atomic
    def save(self, commit=True):
        # Save the Student instance
        student = super().save(commit=False)
        student.role = Student.base_role  # Ensure the role is set to STUDENT
        if commit:
            student.save()
        
        # Create and populate the StudentProfile
        course = self.cleaned_data['course']
        enrolled_subjects = self.cleaned_data['enrolled_subjects']
        StudentProfile.objects.create(
            studentID=student,
            Course=Course
        ).enrolled_subjects.set(enrolled_subjects)

        return student