from django.urls import path
from . import views


name = 'clients'

urlpatterns= [path('', views.client_list, name='client_list'),
              path('client_create', views.client_create, name='client_create'),
              path('client_edit/<str:code>', views.client_edit, name='client_edit'),]