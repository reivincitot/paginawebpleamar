from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Equipos
from .forms import EquiposForm

def is_capitan_or_admin_or_president(user):
    return user.groups.filter(name__in=['Capitan', 'Administrador', 'Presidente']).exists()

@user_passes_test(is_capitan_or_admin_or_president, login_url='/login/')
def equipos_list(request):
    equipos = Equipos.objects.all()
    return render(request, 'equipos/equipos_list.html', {'equipos': equipos})

@user_passes_test(is_capitan_or_admin_or_president, login_url='/login/')
def add_equipo(request):
    if request.method == 'POST':
        form = EquiposForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos_list')
    else:
        form = EquiposForm()
    return render(request, 'equipos/add_equipo.html', {'form': form})
