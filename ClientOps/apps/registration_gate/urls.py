from django.urls import path
from . import views


name='registration_gate'


urlpatterns = [path('create_employ', views.create_employ, name='create_employ'),
               path('show_all_block_employees', views.show_all_block_employees, name='show_all_block_employees')]