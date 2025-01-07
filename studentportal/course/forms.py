from django.forms import ModelForm
from course.models import Course

class add_course(ModelForm):
    class Meta:
        model = Course
        fields = ['id','name']
        labels ={
            "name":""
        }

class edit_course(ModelForm):
    pass