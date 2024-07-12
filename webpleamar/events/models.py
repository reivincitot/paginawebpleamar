from django.db import models
from schedule.models import Event
from django.utils import timezone

class ClubEvent(Event):
    titulo = models.CharField(max_length=100, default="Sin título")
    start_time = models.DateTimeField(default=timezone.now)
    day = models.IntegerField(default=1)
    month = models.IntegerField(default=1)
    year = models.IntegerField(default=2024)
    descripcion = models.TextField(verbose_name="Descripción del evento")

    def __str__(self):
        return self.titulo
