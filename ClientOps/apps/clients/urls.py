from django.urls import path
from . import views


name = 'clients'

urlpatterns= [path('', views.client_list, name='client_list'),
              path('client_create', views.client_create, name='client_create'),
              path('client_edit/<str:code>', views.client_edit, name='client_edit'),
              path('removal_client/<str:code>', views.removal_client, name='removal_client'),
              path('filter_client', views.filter_client, name='filter_client'),
              path('search_client',views.search_client, name='search_client'),
              path('services', views.services, name='services'),]