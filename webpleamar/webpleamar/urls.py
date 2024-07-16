from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_view),
    path('events/', include('events.urls')),
    path('', include('homepage.urls')),
    path('gallery_app/', include('gallery_app.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
