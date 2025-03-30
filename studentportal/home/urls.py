from django.urls import path, include
from home import views

app_name = 'home'

urlpatterns = [
    #CASHIER URLS START =========================

    path('cashier/', views.cashier_home, name='cashier-home'),
    path('cashier/edit-cashier', views.edit_cashier, name='edit-cashier'),
    path('cashier/edit-cashier-password', views.edit_cashier_password, name='edit-cashier-password'),
    path('cashier/unconfirmed-transactions',views.unconfirmed_transaction_cashier,name='unconfirmed-cashier-transactions'),
    path('cashier/confirmed-transactions',views.confirmed_transaction_cashier,name='confirmed-cashier-transactions'),

    #CASHIER URLS END=============================

    #REGISTRAR URLS START ========================
    path('registrar/', views.registrar_dashboard, name='registrar-dashboard'),
    path('registrar/document-request/', views.registrar_document_request, name='document-request'),
    path('registrar/generate-document/', views.registrar_generate_document, name='generate-document'),
    path('registrar/grade-list/', views.registrar_grade_list, name='grade-list'),
    path('registrar/gen-cert/', views.generate_cert, name='generate-cert'),
    path('registrar/gen-cert-success/', views.gen_cert_success, name='generate-cert-success'),


    path('registrar/create-student/', views.registrar_create_student, name='create-student-profile'),





    #REGISTRAR URLS END ========================

    #STUDENT URLS START ========================

    path('student/',views.student_home,name='student-home'),
    path('student/profile',views.student_profile,name='student-profile'),
    path('student/password-change',views.student_edit_password,name='student-password'),
    path('student/request-form',views.student_requestform,name='student-request-form'),
    path('student/newsfeed',views.student_newsfeed,name='student-newsfeed'),
    path('student/transaction-history',views.student_transaction,name='student-transaction'),

    #STUDENT URLS END ========================

    #TEACHER URLS START ========================
    
    path('teacher/',views.teacher_home,name='teacher-home'),
    path('teacher/newsfeed',views.teacher_newsfeed,name='teacher-newsfeed'),
    path('teacher/edit-teacher',views.edit_teacher,name='teacher-edit'),
    path('teacher/edit-teacher-password',views.edit_teacher_password,name='teacher-edit-password'),

    #TEACHER URLS START ========================
    
    path('announcement/', include('news.urls',namespace='news')),
    path('transactions/',include('transactions.urls',namespace='transactions')),
    path('user/',include('users.urls',namespace='users')),
    path('grade-management/',include('grades.urls',namespace='grades'))

]