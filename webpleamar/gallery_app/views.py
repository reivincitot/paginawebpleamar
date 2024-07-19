from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Imagen, Video, Comentario, Like
from .forms import ImagenForm, VideoForm, ComentarioForm
from django.http import JsonResponse


def gallery_view(request):
    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:   
        form = ImagenForm()
        imagenes = Imagen.objects.all()
        return render(request,'gallery_app/gallery.html', {'form': form, 'imagenes': imagenes})

@login_required
def crear_imagen(request):
    if request.method == "POST":
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            imagen = form.save(commit=False)
            imagen.usuario = request.user
            imagen.save()
            return redirect("gallery")
    else:
        form = ImagenForm()
    return render(request, "gallery_app/crear_imagen.html", {"form", form})


@login_required
def crear_video(request):
    if request.method == "POST":
        form = VideoForm(request.POST, request.File)
        if form.is_valid():
            video = form.save(commit=False)
            video.usuario = request.user
            video.save()
            return redirect("gallery")
    else:
        form = VideoForm()
    return render(request, "gallery_app/crear_video.html", {"form": form})


@login_required
def agregar_comentario(request, tipo, id):
    if tipo == "video":
        objeto = get_object_or_404(Video, id=id)
    else:
        objeto = get_object_or_404(Imagen, id=id)

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            if tipo == "video":
                comentario.video = objeto
            else:
                comentario.imagen = objeto
            comentario.save()
            return redirect('gallery')
        else:
            comentario.imagen = objeto
        comentario.save()
        return redirect('gallery')
    return redirect('gallery')


@login_required
def dar_like(request, tipo, id):
    if tipo == "video":
        objeto = get_object_or_404(Video, id=id)
    else:
        objeto = get_object_or_404(Imagen, id=id)

    like, created = Like.objects.get_or_create(
        usuario=request.user,
        video=objeto if tipo == "video" else None,
        imagen=objeto if tipo == "imagen" else None,
    )
    if not created:
        like.delete()
    return redirect('gallery')


@login_required
def editar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id, usuario=request.user)
    if request.method == "POST":
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect(
                "detalle",
                tipo="video" if comentario.video else "imagen",
                id=comentario.video.id if comentario.video else comentario.imagen.id,
            )
        else:
            form = ComentarioForm(instance=comentario)
        return render(request, "gallery_app/editar_comentario.html", {"form": form})


def detalle(request, tipo, id):
    if tipo == "video":
        objeto = get_object_or_404(Video, id=id)
    else:
        objeto = get_object_or_404(Imagen, id=id)

    comentarios = objeto.comentarios.all()
    return render(
        request,
        "gallery_app/detalle.html",
        {"objeto": objeto, "comentarios": comentarios},
    )
