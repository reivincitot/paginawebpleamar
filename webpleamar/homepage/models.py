from django.db import models


class Historia(models.Model):
    contenido = models.TextField(verbose_name="Historia del club")


class Participacion(models.Model):
    nombre_evento = models.CharField(max_length=255, verbose_name="Nombre del Evento")
    fecha = models.DateField(verbose_name="Fecha de participación")
    resultado = models.TextField(verbose_name="Resultado")
