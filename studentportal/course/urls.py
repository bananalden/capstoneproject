from django.urls import path, include
from course import views

app_name = 'course'
urlpatterns = [

    #COURSE LIST ROUTES START
    path('course-list', views.create_course, name='course-list'),
    path('course-list/edit', views.update_course, name='course-edit'),
    path('course-list/delete', views.delete_course, name='course-delete'),
    #COURSE ROUTES END

    #SEMESTER LIST ROUTES START
    path('semester-list', views.create_semester, name='semester-list'),
    path('semester-list/edit', views.update_semester, name='semester-edit'),
    path('semester-list/delete', views.delete_semester, name='semester-delete'),
    #SEMESTER LIST ROUTES END

    #SUBJECT LIST ROUTES START
    path('subject-list', views.create_subject, name='subject-list'),
    path('subject-list/edit', views.update_subject, name='subject-edit'),
    path('subject-list/delete', views.delete_subject, name='subject-delete'),
    #SUBJECT LIST ROUTES END

 
]