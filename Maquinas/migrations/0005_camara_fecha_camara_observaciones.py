# Generated by Django 5.1.3 on 2024-11-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maquinas', '0004_camara_informe_piso_delete_marcador_delete_plano_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='camara',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='camara',
            name='observaciones',
            field=models.TextField(blank=True, null=True),
        ),
    ]
