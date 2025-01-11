from django.urls import path, include
from users import views

app_name = 'users'

urlpatterns =[
    #ADMIN ROUTES START
    path('admin-list',views.create_admin, name='admin-list'),
    path('admin-list/edit',views.update_admin,name='admin-update'),
    #ADMIN ROUTES END

    #CASHIER ROUTES START
    path('cashier-list',views.create_cashier,name='cashier-list'),
    #CASHIER ROUTES END

    #REGISTRAR ROUTES START
    path('registrar-list',views.create_registrar, name='registrar-list'),
    #REGISTRAR ROUTES END

    #TEACHER ROUTES START
    path('teacher-list',views.create_teacher, name='teacher-list'),
    #TEACHER ROUTES END

    #STUDENT ACTION START
    path('student-list', views.create_student, name='student-list')
    #STUDENT ACTION END
]