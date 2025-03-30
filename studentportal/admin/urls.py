from django.urls import path, include
from admin import views as views_admin

app_name = 'admin'
urlpatterns = [
    path('', views_admin.admin_login, name='admin-login'),
    path('home/', views_admin.home, name='dashboard'),
    path('edit-admin/',views_admin.edit_admin_user,name='edit-admin'),
    path('edit-admin-password',views_admin.edit_admin_password,name='edit-admin-password'),
    path('newsfeed-list',views_admin.admin_newsfeed,name='admin-newsfeed'),
    path('newsfeed-edit',views_admin.edit_news_item,name='edit-news'),
    path('newsfeed-delete',views_admin.delete_news_item,name='delete-news'),
    path('usermanagement/', include('users.urls', namespace='usermanagement')),
    path('transactionmanagement/',include('transactions.urls', namespace='transactions'))
]