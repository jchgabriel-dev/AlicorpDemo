from django.db import models


class Piso(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='Planos/')  

    def __str__(self):
        return self.nombre


class Camara(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    codigo = models.CharField(max_length=100, blank=True, null=True)
    ip = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    piso = models.ForeignKey(Piso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

 
class Informe(models.Model):
    camara = models.ForeignKey(Camara, on_delete=models.CASCADE, blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True) 
    descripcion = models.TextField(blank=True, null=True) 
    autor = models.CharField(max_length=100, blank=True, null=True)  

    



