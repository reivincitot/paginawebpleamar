# equipos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipos_list, name='equipos_list'),
    path('add/', views.add_equipo, name='add_equipo'),
]
