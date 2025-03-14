from django.urls import path, include
from grades import views

app_name = 'grades'

urlpatterns =[
    path('grade-upload/',views.grade_upload,name='grade-upload')
]