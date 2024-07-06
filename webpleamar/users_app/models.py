from django.db import models
from django.contrib.auth.models import AbstractUser


class Equipo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del equipo")

    def __str__(self):
        return self.nombre

    
class CustomUser(AbstractUser):
    birth_day = models.DateField(null=True, blank=True, verbose_name="Fecha de nacimiento")
    address = models.CharField(max_length=255, blank=True, verbose_name="Dirección")
    phone_number = models.CharField(max_length=12, blank=True, verbose_name="Número Telefónico")
    team = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Equipo")
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")

    class Meta:
        verbose_name = "Usuario personalizado"
        verbose_name_plural = "Usuarios Personalizados"

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permission',
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser'
    )
