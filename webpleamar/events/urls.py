from django.urls import path
from .views import club_calendar_view

urlpatterns = [
    path('events/', club_calendar_view, name='club_calendar'),
    ]
