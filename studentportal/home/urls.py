from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('cashier/', views.cashier_home, name='cashier-home'),
    path('cashier/transactions',views.transaction_cashier,name='cashier-transactions'),
    path('registrar/', views.registrar_home, name='registrar-home')
]