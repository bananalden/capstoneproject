from django.urls import path
from news import views

app_name = 'news'

urlpatterns = [
    path('create-announcement/',views.create_announcements, name='create-announcement')

]