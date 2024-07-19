# Generated by Django 4.2.13 on 2024-07-18 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='imagen',
            name='fecha_de_subida',
        ),
        migrations.RemoveField(
            model_name='video',
            name='fecha_de_subida',
        ),
        migrations.AddField(
            model_name='comentario',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='imagen',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='imagen',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='video',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='video',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='video',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]