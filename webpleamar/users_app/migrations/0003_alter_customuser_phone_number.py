# Generated by Django 4.2 on 2024-07-01 04:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users_app", "0002_rename_equip_customuser_team"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="phone_number",
            field=models.CharField(
                blank=True, max_length=9, verbose_name="Número telefónico"
            ),
        ),
    ]