from django.db import models
from django.conf import settings


class Imagen(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=255)
    fecha_de_subida = models.DateField(auto_now=True)
    archivo_imagen = models.ImageField(upload_to='imagenes/')

class Video(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=255)
    fecha_de_subida = models.DateField(auto_now=True)
    archivo_video = models.FileField(upload_to='videos/')

class Comentario(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comentarios", null=True, blank=True)
    imagen = models.ForeignKey(Imagen, on_delete=models.CASCADE, related_name="comentarios", null=True, blank=True )

class Like(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='Like', null=True, blank=True)
    imagen = models.ForeignKey(Imagen, on_delete=models.CASCADE, related_name='Like', null=True, blank=True)

    class Meta:
        unique_together = ('usuario', 'video', 'imagen')