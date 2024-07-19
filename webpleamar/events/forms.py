from django import forms
from .models import ClubEvent, Torneo

class ClubEventForm(forms.ModelForm):
    class Meta:
        model = ClubEvent
        fields = ['titulo', 'start_time', 'day', 'month', 'year', 'descripcion']

class TorneoForm(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = ['nombre', 'puesto']
