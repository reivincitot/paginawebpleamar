from django import forms
from .models import Imagen, Video, Comentario


class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ['archivo_imagen', 'titulo', 'descripcion']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['archivo_video', 'titulo', 'descripcion']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']