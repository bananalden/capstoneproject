from django.urls import path, include
from course import views

app_name = 'course'
urlpatterns = [

    #COURSE LIST CONTROLLERS START
    path('course-list', views.create_course, name='course-list'),
    path('get-course-data/<int:pk>', views.get_coursedata, name='get_model_data'),
    path('course-list/edit', views.update_course, name='course-edit'),
    path('course-list/delete', views.delete_course, name='course-delete'),
    #COURSE CONTROLLERS END
    #SEMESTER LIST CONTROLLERS START
    path('semester-list', views.create_semester, name='semester-list'),
    path('get-semester-data/<int:pk>', views.get_semesterdata, name='get_semester_data'),
    path('semester-list/edit', views.update_semester, name='semester-edit'),
    path('semester-list/delete', views.delete_semester, name='semester-delete'),
    #SEMESTER LIST CONTROLLERS END
    path('subject-list', views.create_subject, name='subject-list'),
    path('get-subject-data/<int:pk>', views.get_subjectdata, name='get_subject_data'),
    path('subject-list/edit', views.update_subject, name='subject-edit'),
        path('subject-list/delete', views.delete_subject, name='subject-delete'),
    #APIS START
    path('api/courses', views.get_course_list, name='get-course-list')
    #APIS END
]