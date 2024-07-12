from django import forms
from .models import ClubEvent

class ClubEventForm(forms.ModelForm):
    class Meta:
        model = ClubEvent
        fields = ['titulo', 'start_time', 'day', 'month', 'year', 'descripcion']
