from django import forms
from .models import Equipos

class EquiposForm(forms.ModelForm):
    class Meta:
        model = Equipos
        fields = ['nombre_equipo','capitan_equipo','participante_2','participante_3','participante_5']