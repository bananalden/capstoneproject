from django.urls import path
from transactions import views
 
app_name='transactions'

urlpatterns = [
        #CRUD PAYMENT PURPOSE START

        #CRUD PAYMENT PURPOSE END
        path('student-payment-request/',views.student_payment_request,name='student-payment-request'),
        path('confirm-transaction/',views.confirm_payment,name='confirm-payment'),


]