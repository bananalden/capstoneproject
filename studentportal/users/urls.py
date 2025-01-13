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
    #REGISTRAR ROUTES END

    #TEACHER ROUTES START
    path('teacher-list',views.create_teacher, name='teacher-list'),
    #TEACHER ROUTES END

    #STUDENT ACTION START
    path('student-list', views.create_student, name='student-list')
    #STUDENT ACTION END
]