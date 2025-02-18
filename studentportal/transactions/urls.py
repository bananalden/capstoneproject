from django.urls import path
from transactions import views
 
app_name='transactions'

urlpatterns = [
        path('create-payment-purpose/',views.create_payment_purpose,name='create-payment-purpose'),
        path('edit-payment-purpose/',views.edit_payment_purpose,name='edit-payment-purpose'),
        path('delete-payment-purpose/',views.delete_payment_purpose,name='delete-payment-purpose'),
]