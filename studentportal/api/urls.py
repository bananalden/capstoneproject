from django.urls import path
from api import views
 
app_name='api'

urlpatterns = [
    #USER APIS START
    path('get-user-object/<int:pk>',views.get_userdata,name='get-admin-object'),
    path('get-cashiers/',views.get_cashier,name="get-cashiers"),
    path('get-registrars/',views.get_registrar,name="get-registrars"),
    path('get-teachers/',views.get_teacher,name="get-teachers"),
    path('get-students/',views.get_student,name="get-students"),
    
    
    
    #USER APIS END
    
    #NEWS API START
    path('get-news/',views.news_list,name='news-list'),
    path('get-news-page/',views.get_news,name='news-page'),
    path('get-news-object/<int:pk>',views.get_news_object,name='get_news_object'),
    #NEWS API END
    
    #GRADES API START
    path('get-grades/',views.get_grades,name='grade-list'),
    path('get-grade-object/<int:pk>',views.get_specific_grade,name='get-grade-object'),
    #GRADES API END

    #TRANSACTION API START
    path('get-payment-data/<int:pk>',views.get_payment_data,name='get-payment-data'),
    path('get-transaction-page-unconfirmed/',views.cashier_transaction_data_unconfirmed,name='cashier-transaction-unconfirmed'),
    path('get-transaction-page-confirmed/',views.cashier_transaction_data_confirmed,name='cashier-transaction-confirmed'),
    path('get-registrar-transaction-page/',views.registrar_doc_list,name='registrar-doc-list'),
    path('get-registrar-complete-page/',views.registrar_complete_list,name='registrar-complete-list'),
    path('export-transaction-report/',views.export_transaction,name="export-transaction"),
    path('student-transaction-history/',views.student_transaction_list,name="student-transaction-history")
    #TRANSACTION API END





]