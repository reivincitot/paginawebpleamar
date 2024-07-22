from django.db import models
from users_app.models import CustomUser


class Equipos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_equipo = models.CharField(max_length=10, verbose_name="Nombre del equipo")
    capitan_equipo = models.ForeignKey(CustomUser, related_name="capitan_equipo", on_delete=models.CASCADE)
    participante_2 = models.ForeignKey(CustomUser, related_name="equipo_participante_2", on_delete=models.CASCADE)
    participante_3 = models.ForeignKey(CustomUser, related_name="equipo_participante_3",on_delete=models.CASCADE)
    participante_4 = models.ForeignKey(CustomUser, related_name="equipo_participante_4",on_delete=models.CASCADE)
    participante_5 = models.ForeignKey(CustomUser, related_name="equipo_participante_5",on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_equipo
