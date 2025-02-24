from django.urls import path, include
from home import views

app_name = 'home'

urlpatterns = [
    #CASHIER URLS START =========================

    path('cashier/', views.cashier_home, name='cashier-home'),
    path('cashier/edit-cashier', views.edit_cashier, name='edit-cashier'),
    path('cashier/unconfirmed-transactions',views.unconfirmed_transaction_cashier,name='unconfirmed-cashier-transactions'),
    path('cashier/confirmed-transactions',views.confirmed_transaction_cashier,name='confirmed-cashier-transactions'),

    #CASHIER URLS END=============================

    #REGISTRAR URLS START ========================

    path('registrar/', views.registrar_home, name='registrar-home'),

    #REGISTRAR URLS END ========================

    #STUDENT URLS START ========================

    path('student/',views.student_home,name='student-home'),
    path('student/profile',views.student_profile,name='student-profile'),
    path('student/request-form',views.student_requestform,name='student-request-form'),
    path('student/newsfeed',views.student_newsfeed,name='student-newsfeed'),

    #STUDENT URLS END ========================

    #TEACHER URLS START ========================
    
    path('teacher/',views.teacher_home,name='teacher-home'),
    path('teacher/newsfeed',views.teacher_newsfeed,name='teacher-newsfeed'),

    #TEACHER URLS START ========================
    
    path('announcement/', include('news.urls',namespace='news')),
    path('transactions/',include('transactions.urls',namespace='transactions'))

]