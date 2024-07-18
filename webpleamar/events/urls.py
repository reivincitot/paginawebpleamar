from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('<int:id>/', views.event_detail, name='event_detail'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('add/', views.add_event, name='add_event'),
    path('add_torneo/', views.add_torneo, name='add_torneo'),
]
