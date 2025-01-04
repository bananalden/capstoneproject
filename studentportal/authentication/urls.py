from django.urls import path, include
from authentication import views

urlpatterns = [
    path('', views.home, name='home'),
    path('401',views.unauthorized_view, name='unauthorized-view')
]