from django.urls import path, include
from authentication import views
from django.contrib.auth import views as auth_views

app_name = 'authentication'

urlpatterns = [
    path('', views.home, name='login'),
    path('logout',views.logout_user,name='logout'),
    path('401',views.unauthorized_view, name='unauthorized-view'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='forgot-password.html'), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_email.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_success/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]