from django.urls import path
from . import views

app_name = 'gallery_app'

urlpatterns = [
    path('', views.gallery, name='gallery'),
]
