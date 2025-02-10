from django.urls import path
from api import views
 
app_name='api'

urlpatterns = [
#================== SCHOOL MANAGEMENT START ============================#
    
#================== SCHOOL MANAGEMENT END ============================#
    path('get-user-object/<int:pk>',views.get_userdata,name='get-admin-object'),
    path('get-teacher-list',views.get_teacher_list,name='get-teacher-list')






]