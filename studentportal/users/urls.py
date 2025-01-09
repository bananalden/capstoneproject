from django.urls import path, include
from users import views

app_name = 'users'

urlpatterns =[
    #ADMIN ROUTES START
    path('admin-list',views.create_admin, name='admin-list'),
]