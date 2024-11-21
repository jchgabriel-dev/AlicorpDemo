from django.db import models



class Marcador(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Plano(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='Planos/')  

    def __str__(self):
        return self.nombre

