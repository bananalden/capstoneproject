from django.urls import path, include
from admin import views

urlpatterns = [
    path('',views.home, name='admin-dashboard'),
    path('course-list', views.create_course, name='create-course'),
    path('semester-list', views.create_semester, name='create-semester'),
    path('subject-list', views.create_subject, name='create-subject'),
    path('admin-list', views.create_admin, name='create-admin'),
    path('teacher-list', views.create_teacher, name='create-teacher')
]