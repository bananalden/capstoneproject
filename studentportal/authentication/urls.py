from django.urls import path, include, reverse_lazy
from authentication import views
from django.contrib.auth import views as auth_views

app_name = 'authentication'

urlpatterns = [
    path('', views.home, name='login'),
    path('auth-regular-user/',views.login_regular_user, name='log-reg-user'),
    path('auth-admin-user/',views.login_admin, name='log-admin'),
    path('logout',views.logout_user,name='logout'),
    path('401',views.unauthorized_view, name='unauthorized-view'),

    #PASSWORD RESET LINKS
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html', email_template_name='registration/password_reset_email.html', success_url=reverse_lazy('authentication:password_reset_done')), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('authentication:password_reset_complete')), name="password_reset_confirm"),
    path('reset_success/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    #PASSWORD RESET LINKS
    
    #MIDDLEWARE BS START
    path('first-login-password/', views.first_log_password  , name='first-login-password'),
    #MIDDLEWARE BS END


    # EMAIL SENT
     path('email-sent/', views.email_sent, name='email-sent'),

     path('set-new-pass/', views.set_new_pass, name='set-new-pass'),

     path('pass-success/', views.pass_success, name='pass-success'),

]