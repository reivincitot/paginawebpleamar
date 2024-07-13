from django.shortcuts import render
from .forms import ParticipacionForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    form = ParticipacionForm()
    user_has_perm = request.user.has_perm('admin') or request.user.has_perm('presidente')

    context = {
        'form':form,
        'user_has_perm': user_has_perm
    }
    return render(request, 'homepage/home.html')

def participacion_torneos(request):
    if request.method == 'POST':
        form = ParticipacionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
        form = ParticipacionForm()

    context = {
        'form': form,
    }
    return render(request, 'homepage/home.html', context)