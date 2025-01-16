from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('cashier/', views.cashier_home, name='cashier-home'),
    path('registrar/', views.registrar_home, name='registrar-home')
]