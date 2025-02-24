from django.urls import path
from api import views
 
app_name='api'

urlpatterns = [

    path('get-user-object/<int:pk>',views.get_userdata,name='get-admin-object'),
    path('get-news/',views.news_list,name='news-list'),
    path('get-news-page/',views.get_news,name='news-page'),
    path('get-payment-data/<int:pk>',views.get_payment_data,name='get-payment-data'),
    path('get-transaction-page-unconfirmed/',views.cashier_transaction_data_unconfirmed,name='cashier-transaction-unconfirmed'),
    path('get-transaction-page-confirmed/',views.cashier_transaction_data_confirmed,name='cashier-transaction-unconfirmed'),
    path('export-transaction-report/',views.export_transaction,name="export-transaction")





]