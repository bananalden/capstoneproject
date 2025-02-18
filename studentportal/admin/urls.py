from django.urls import path, include
from admin import views as views_admin

app_name = 'admin'
urlpatterns = [
    path('', views_admin.home, name='dashboard'),
    path('edit-admin/',views_admin.edit_admin_user,name='edit-admin'),
    path('edit-admin-password',views_admin.edit_admin_password,name='edit-admin-password'),
    path('add-payment-purpose',views_admin.payment_purpose_list,name='payment-purpose-list'),
    path('usermanagement/', include('users.urls', namespace='usermanagement'))
]