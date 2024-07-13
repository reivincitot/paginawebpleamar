from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('participacion/', views.participacion_torneos, name='participacion_torenos')
]
