from django import forms
from .models import Participacion

class ParticipacionForm(forms.ModelForm):
    class Meta:
            model = Participacion
            fields = ['nombre_evento','fecha','descripcion']