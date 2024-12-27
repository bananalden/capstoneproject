from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('studentdashboard', views.studentview, name='studentdashboard'),
    path('registrarview', views.registrarview, name='registrardashboard'),
    path('cashierview', views.cashierrview, name='cashierdashboard'),
    path('facultyview', views.facultyview, name='facultydashboard'),
    path('moderator', views.moderatorview, name='moderatordashboard'),
    path('createuser', views.createuser, name='createuser'),
    path('accessdenied',views.accessdenied, name='accessdenied'),
    path('logout', views.logout_user, name='logout'),

]