from django.urls import path, include
from authentication import views

urlpatterns = [
    path('', views.home, name='home')
]