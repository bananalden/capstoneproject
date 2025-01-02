from django.contrib import admin
from .models import Course, Subject

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display =['course_id']

class SubjectAdmin(admin.ModelAdmin):
    list_display =['subject_name']    

admin.site.register(Course)


