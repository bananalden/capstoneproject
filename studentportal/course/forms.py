from django.forms import ModelForm
from course.models import Course, Semester, Subject

class add_course(ModelForm):
    class Meta:
        model = Course
        fields = ['id','name']
        labels ={
            "name":""
        }

class add_semester(ModelForm):
    class Meta:
        model = Semester
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            self.field.widget.attrs['class'] = 'form-group'

class add_subject(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'