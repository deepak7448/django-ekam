from django.urls import path
from django.conf.urls import include, url
from .import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .forms import EmailValidationOnForgotPassword


urlpatterns = [
    #path('', login_required(TemplateView.as_view(template_name='core/home.html')), name='home')
    path('booking/',views.booking, name='booking'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/profile/', views.view_profile, name='view_profile'),
    path('accounts/profile/edit/', views.edit_profile, name='edit_profile'),
    path('accounts/password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
        name='password_change_done'),

    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), 
        name='password_change'),

    path('accounts/password_reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),
     name='password_reset_done'),

    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset.html'), name='password_reset_confirm'),

    #path('accounts/password_reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html',form_class=EmailValidationOnForgotPassword), name='password_reset'),
    path('accounts/reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
     name='password_reset_complete'),
    path('oauth/', include('social_django.urls', namespace="socail")),


    #path('/accounts/logout/', views.logout, name='logout'),
   # path('oauth/', include('social_django.urls', namespace="socail")),
    # path('login/', auth_views.MyView.as_view()),


]
