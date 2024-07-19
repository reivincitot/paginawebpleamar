from django.urls import path
from . import views


urlpatterns = [
    path('', views.gallery_view, name='gallery'),
    path("crear/imagen/", views.crear_imagen, name="crear_imagen"),
    path("crear/video/", views.crear_video, name="crear_video"),
    path("detalle/<str:tipo>/<int:id>/", views.detalle, name="detalle"),
    path(
        "comentario/agregar/<str:tipo>/<int:id>/",
        views.agregar_comentario,
        name="agregar_comentario",
    ),
    path("like/<str:tipo>/<int:id>/", views.dar_like, name="dar_like"),
    path(
        "comentario/editar/<int:comentario_id>/",
        views.editar_comentario,
        name="editar_comentario",
    ),
]
