# Generated by Django 5.1.3 on 2024-11-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maquinas', '0005_camara_fecha_camara_observaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='informe',
            name='codigo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='informe',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='informe',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]
