from django.db import models
from schedule.models import Event


class ClubEvent(Event):
    descripcion = models.TextField(verbose_name="Descripción del evento")
    resultado = models.TextField(verbose_name="Resultado del evento", blank=True, null=True)

    def __str__(self):
        return self.title
