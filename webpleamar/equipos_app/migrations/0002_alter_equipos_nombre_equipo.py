# Generated by Django 4.2.13 on 2024-07-20 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipos',
            name='nombre_equipo',
            field=models.TextField(max_length=10, verbose_name='Nombre del equipo'),
        ),
    ]
