from django.urls import path
from . import views

urlpatterns = [
    path('', views.vibewire_list, name ='vibewire_list'),
    path('create/', views.vibewire_create, name ='vibewire_create'),
    path('<int:vibewire_id>/edit/', views.vibewire_edit, name ='vibewire_edit'),
    path('<int:vibewire_id>/delete/', views.vibewire_delete, name ='vibewire_delete'),
    path('register/', views.register, name='register'),
] 
