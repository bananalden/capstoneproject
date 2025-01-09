from django.urls import path, include
from admin import views as views_admin

app_name = 'admin'
urlpatterns = [
    path('', views_admin.home, name='dashboard'),
    path('schoolmanagement/', include('course.urls', namespace='schoolmanagement')),
    path('usermanagement/', include('users.urls', namespace='usermanagement'))
]