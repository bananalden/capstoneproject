from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'),
    #STUDENT URLS START
    path('studentdashboard', views.studentview, name='studentdashboard'),
    #STUDENT URLS END

    #REGISTRAR URLS START
    path('registrarview', views.registrarview, name='registrardashboard'),
    #REGISTRAR URLS END

    #CASHIER URLS START
    path('cashierview', views.cashierrview, name='cashierdashboard'),
    #CASHIER URLS END

    #FACULTY URLS START
    path('facultydashboard', views.facultyview, name='facultydashboard'),
    #FACULTY URLS END

    #MODERATOR URLS START
    path('moderatordashboard', views.moderatorview, name='moderatordashboard'),
    # MODERATOR URLS END
    path('createuser', views.createuser, name='createuser'),
    path('accessdenied',views.accessdenied, name='accessdenied'),

    #MISC START
    path('logout', views.logout_user, name='logout'),
    #MISC END
]