from django.urls import path, include
from users import views

app_name = 'users'

urlpatterns =[

    path('dashboard-action',views.admin_dashboard_action,name='dashboard-action'),
    path('edit-user',views.edit_user,name='edit-user'),
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
    path('student-list/edit',views.update_student,name='student-update'),
    path('student-list/delete',views.delete_student, name='student-delete'),
    #STUDENT ACTION END

    #USER ACTION START
    path('edit-password',views.change_password_user,name='change-password'),
    path('edit-user',views.change_password_user,name='change-password'),
    path('edit-student-profile',views.student_profile_update,name='student-profile-update')
    #USER ACTION END

]