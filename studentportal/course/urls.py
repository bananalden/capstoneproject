from django.urls import path, include
from course import views

app_name = 'course'
urlpatterns = [
    path('course-list', views.create_course, name='course-list'),
    path('semester-list', views.create_semester, name='semester-list'),
    path('subject-list', views.create_subject, name='subject-list')
]