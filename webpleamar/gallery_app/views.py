from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


def gallery(request):
    return render(request, 'gallery_app/gallery.html')
