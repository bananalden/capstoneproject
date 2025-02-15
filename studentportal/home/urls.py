from django.urls import path, include
from home import views

app_name = 'home'

urlpatterns = [
    #CASHIER URLS START =========================

    path('cashier/', views.cashier_home, name='cashier-home'),
    path('cashier/transactions',views.transaction_cashier,name='cashier-transactions'),

    #CASHIER URLS END=============================

    #REGISTRAR URLS START ========================

    path('registrar/', views.registrar_home, name='registrar-home'),

    #REGISTRAR URLS END ========================

    #STUDENT URLS START ========================

    path('student/',views.student_home,name='student-home'),
    path('student/profile',views.student_profile,name='student-profile'),
    path('student/newsfeed',views.student_newsfeed,name='student-newsfeed'),

    #STUDENT URLS END ========================

    
    path('teacher/',views.teacher_home,name='teacher-home'),
    path('teacher/teachernewsfeed',views.teacher_newsfeed,name='teacher-newsfeed'),

    #STUDENT URLS START ========================
    path('announcement/', include('news.urls',namespace='news'))


]