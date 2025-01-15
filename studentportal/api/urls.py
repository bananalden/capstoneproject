from django.urls import path
from api import views
 
app_name='api'

urlpatterns = [
#================== SCHOOL MANAGEMENT START ============================#
    
    path('get-course-list',views.get_course_list,name='get-course-list'),
    path('get-course-object/<int:pk>',views.get_coursedata,name='get-course-object'),
    path('get-semester-list',views.get_semester_list,name='get-semester-list'),
    path('get-semester-object/<int:pk>',views.get_semesterdata,name='get-semester-object'),
    path('get-subject-object/<int:pk>',views.get_subjectdata,name='get-subject-object'),

#================== SCHOOL MANAGEMENT END ============================#
    path('get-user-object/<int:pk>',views.get_userdata,name='get-admin-object'),






]