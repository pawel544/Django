from django.urls import path
from . import views
#from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

app_name = 'accounts'

urlpatterns = [path('login/', views.login_user, name='login'),
               path('signupuser/', views.signupuser, name='signupuser'),
               path('change_password', views.change_password, name='change_password'),]