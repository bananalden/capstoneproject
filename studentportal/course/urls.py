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
    path('semester-list', views.create_semester, name='semester-list'),
    path('subject-list', views.create_subject, name='subject-list')
]