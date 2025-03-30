from django import forms
from grades.models import Grades

class edit_grade(forms.ModelForm):

    class Meta:
        model = Grades
        fields = ["grade_value"]
