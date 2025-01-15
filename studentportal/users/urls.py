from django.urls import path, include
from users import views

app_name = 'users'

urlpatterns =[
    #ADMIN ROUTES START
    path('admin-list',views.create_admin, name='admin-list'),
    path('admin-list/edit',views.update_admin,name='admin-update'),
    path('admin-list/delete',views.delete_admin,name='admin-delete'),
    #ADMIN ROUTES END

    #CASHIER ROUTES START
    path('cashier-list',views.create_cashier,name='cashier-list'),
    path('cashier-list/edit',views.update_cashier,name='cashier-update'),
    path('cashier-list/delete',views.delete_cashier, name='cashier-delete'),
    #CASHIER ROUTES END

    #REGISTRAR ROUTES START
    path('registrar-list',views.create_registrar, name='registrar-list'),
    path('registrar-list/edit',views.update_registrar, name='registrar-update'),
    path('registrar-list/delete',views.delete_registrar,name='registrar-delete'),
    #REGISTRAR ROUTES END

    #TEACHER ROUTES START
    path('teacher-list',views.create_teacher, name='teacher-list'),
    path('teacher-list/edit',views.update_teacher, name='teacher-update'),
    path('teacher-list/delete',views.delete_teacher,name='teacher-delete'),
    #TEACHER ROUTES END

    #STUDENT ACTION START
    path('student-list', views.create_student, name='student-list'),
    path('student-list/edit',views.update_student,name='student-update')
    #STUDENT ACTION END
]