from django.db import models
from schedule.models import Event
from django.utils import timezone
from django.contrib.auth.models import User

class ClubEvent(Event):
    titulo = models.CharField(max_length=100, default="Sin título")
    start_time = models.DateTimeField(default=timezone.now)
    day = models.IntegerField(default=1)
    month = models.IntegerField(default=1)
    year = models.IntegerField(default=2024)
    descripcion = models.TextField(verbose_name="Descripción del evento")

    def __str__(self):
        return self.titulo


class Torneo(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_add_torneo","Can add torneo"),
        ]

    def __str__(self):
        return self.nombre
    