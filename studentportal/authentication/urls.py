from django.urls import path, include
from authentication import views

app_name = 'authentication'

urlpatterns = [
    path('', views.home, name='login'),
    path('logout',views.logout_user,name='logout'),
    path('401',views.unauthorized_view, name='unauthorized-view')
]