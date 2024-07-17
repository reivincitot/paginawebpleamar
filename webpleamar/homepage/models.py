from django.db import models


class Historia(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField(verbose_name="Historia del club")

    def __str__(self):
        return self.titulo