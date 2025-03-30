from django import forms
from grades.models import Grades
from decimal import Decimal, InvalidOperation

class edit_grade(forms.ModelForm):

    class Meta:
        model = Grades
        fields = ["grade_value"]

    def clean_grade_value(self):
        grade_value = self.cleaned_data.get('grade_value')
        try:
            grade_value = Decimal(str(grade_value))
        except (InvalidOperation, TypeError):
            raise forms.ValidationError("Invalid grade value. Please enter a valid number")
        
        if grade_value < 0 or grade_value > 100:
            raise forms.ValidationError("Grade value must be between 0 and 100")
        
        return grade_value
