from django.urls import path
from api import views
 
app_name='api'

urlpatterns = [

    path('get-user-object/<int:pk>',views.get_userdata,name='get-admin-object'),







]