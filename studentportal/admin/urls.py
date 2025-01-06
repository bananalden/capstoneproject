from django.urls import path, include
from admin import views

urlpatterns = [
    path('',views.home, name='admin-dashboard'),
    path('course-list', views.create_course, name='create-course'),
    path('semester-list', views.create_semester, name='create-semester'),
    path('subject-list', views.create_subject, name='create-subject'),
]