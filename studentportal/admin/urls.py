from django.urls import path, include
from admin import views

urlpatterns = [
    path('',views.home, name='admin-dashboard'),
    path('user-management', views.user_management, name='user-management')
]