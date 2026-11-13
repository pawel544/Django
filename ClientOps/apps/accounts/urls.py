from django.urls import path
from . import views
#from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

app_name = 'accounts'

urlpatterns = [path('login/', views.login_user, name='login'),]