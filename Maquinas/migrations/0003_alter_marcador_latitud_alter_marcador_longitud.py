# Generated by Django 5.1.3 on 2024-11-21 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maquinas', '0002_plano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marcador',
            name='latitud',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='marcador',
            name='longitud',
            field=models.FloatField(blank=True, null=True),
        ),
    ]