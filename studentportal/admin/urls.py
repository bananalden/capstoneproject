from django.urls import path, include
from admin import views as views_admin

app_name = 'admin'
urlpatterns = [
    path('', views_admin.home, name='dashboard'),
    path('admin-list', views_admin.create_admin, name='useradmin'),
    path('teacher-list', views_admin.create_teacher, name='userteacher'),
    path('student-list', views_admin.create_student, name='userstudent'),
    path('cashier-list', views_admin.create_cashier, name='usercashier'),
    path('registrar-list', views_admin.create_registrar, name='userregistrar')
]