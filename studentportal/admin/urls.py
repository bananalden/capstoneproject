from django.urls import path, include
from admin import views

urlpatterns = [
    path('',views.home, name='admin-dashboard'),
    path('course-list', views.create_course, name='create-course')
]