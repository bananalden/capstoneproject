from django.urls import path
from transactions import views
 
app_name='transactions'

urlpatterns = [
        #CRUD PAYMENT PURPOSE START

        #CRUD PAYMENT PURPOSE END
        path('student-payment-request/',views.student_payment_request,name='student-payment-request'),
        path('confirm-transaction/',views.confirm_payment,name='confirm-payment'),
        path('manual_request/', views.manual_request, name="manual-transaction"),
        path('complete-request/', views.complete_docu_request, name='complete-request'),
        path('cancel-request/', views.cancel_docu_request, name='cancel-request')

]