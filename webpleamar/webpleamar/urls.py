from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users_app import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', user_views.login_view, name='login'),
    path('accounts/logout/', user_views.logout_view, name='logout'),  # Utiliza la función logout_view de users_app
    path('events/', include('events.urls')),
    path('', include('homepage.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
