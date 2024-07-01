from django.db import models
from django.contrib.auth.models import AbstractUser

class Equipo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del equipo")

    def __str__(self):
        return self.nombre

class CustomUser(AbstractUser):
    """
    Extiende el modelo de usuario predeterminado de Django con campos personalizados.
    """
    first_name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")
    username = models.CharField(max_length=100, unique=True, verbose_name="Nombre de usuario")
    birth_day = models.DateField(null=True, blank=True, verbose_name="Fecha de nacimiento")
    address = models.CharField(max_length=255, blank=True, verbose_name="Dirección")
    phone_number = models.CharField(max_length=9, blank=True, verbose_name="Número telefónico")
    email = models.EmailField(max_length=255, blank=True, verbose_name="Correo electrónico")
    team = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Equipo")

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",
        blank=True,
        help_text="El grupo al que pertenece este usuario. Se le concederán los permisos correspondientes",
        verbose_name="Permisos de usuario"
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customer_user_permissions_set",
        blank=True,
        help_text="Permisos específicos para este usuario",
        verbose_name="Permisos de usuario"
    )

    class Meta:
        verbose_name = "Usuario personalizado"
        verbose_name_plural = "Usuarios personalizados"

class PiezaDePesca(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Usuario")
    especie = models.CharField(max_length=50, blank=True, verbose_name="Especie")
    peso = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peso")
    longitud = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Longitud")
    metodo_de_pesca = models.CharField(max_length=100, blank=True, verbose_name="Método de pesca")

    def __str__(self):
        return f"Pieza de {self.usuario.username} - especie {self.especie}, {self.peso}kg, {self.longitud}cm"
