from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('operator/', views.operator_panel,
         name='operator'),
]