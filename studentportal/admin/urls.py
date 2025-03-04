from django.urls import path, include
from admin import views as views_admin

app_name = 'admin'
urlpatterns = [
    path('', views_admin.admin_login, name='admin-login'),
    path('home/', views_admin.home, name='dashboard'),
    path('edit-admin/',views_admin.edit_admin_user,name='edit-admin'),
    path('edit-admin-password',views_admin.edit_admin_password,name='edit-admin-password'),
    path('usermanagement/', include('users.urls', namespace='usermanagement')),
    path('transactionmanagement/',include('transactions.urls', namespace='transactions'))
]