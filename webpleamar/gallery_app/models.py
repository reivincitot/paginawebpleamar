from django.db import models
from django.conf import settings
from django.utils import timezone

class Imagen(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)  # Proporciona un valor predeterminado
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    archivo_imagen = models.ImageField(upload_to="imagenes/")
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

class Video(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)  # Proporciona un valor predeterminado
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    archivo_video = models.FileField(upload_to="videos/")
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)  # Proporciona un valor predeterminado
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name="comentarios",
        null=True,
        blank=True,
    )
    imagen = models.ForeignKey(
        Imagen,
        on_delete=models.CASCADE,
        related_name="comentarios",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Comentario de {self.usuario} en {"Video" if self.video else "Imagen"}'

class Like(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE, related_name="Like", null=True, blank=True
    )
    imagen = models.ForeignKey(
        Imagen, on_delete=models.CASCADE, related_name="Like", null=True, blank=True
    )

    class Meta:
        unique_together = ("usuario", "video", "imagen")
