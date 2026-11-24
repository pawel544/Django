from django.urls import path
from . import views


name='registration_gate'


urlpatterns = [path('', views.create_employ, name='create_employ')]