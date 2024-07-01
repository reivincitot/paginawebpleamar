from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
