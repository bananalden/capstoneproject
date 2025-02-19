from django.urls import path
from transactions import views
 
app_name='transactions'

urlpatterns = [
        #CRUD PAYMENT PURPOSE START
        path('create-payment-purpose/',views.create_payment_purpose,name='create-payment-purpose'),
        path('edit-payment-purpose/',views.edit_payment_purpose,name='edit-payment-purpose'),
        path('delete-payment-purpose/',views.delete_payment_purpose,name='delete-payment-purpose'),
        #CRUD PAYMENT PURPOSE END
        path('student-payment-request/',views.student_payment_request,name='student-payment-request'),


]