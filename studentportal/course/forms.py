from django.forms import ModelForm
from django.core.exceptions import ValidationError
from course.models import Course, Semester, Subject

class add_course(ModelForm):
    class Meta:
        model = Course
        fields = ['id','name']
        labels ={
            "name":""
        }

        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get('name')

            if self.instance.pk and Course.objects.filter(name=name).exclude(pk=self.instance.pk).exists():
                msg = "Course name already exists!"
                self.add_error("name", msg)

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