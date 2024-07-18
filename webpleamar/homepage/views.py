from django.shortcuts import render
from events.models import Torneo


def home(request):
    torneos = Torneo.objects.all()
    return render(request, 'homepage/home.html', {'torneos': torneos})
