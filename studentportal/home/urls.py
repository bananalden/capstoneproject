from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('studentview', views.studentview, name='studentview'),
    path('registrarview', views.registrarview, name='registrarview'),
    path('cashierview', views.cashierrview, name='cashierview'),
    path('facultyview', views.facultyview, name='facultyview'),
    path('createuser', views.createuser, name='createuser'),
    path('accessdenied',views.accessdenied, name='accessdenied'),
    path('logout', views.logout_user, name='logout')

]