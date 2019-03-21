from django.db import models
from django.urls import reverse


class provincia(models.Model):
    nombre = models.CharField(max_length=15)

class proveedor(models.Model):
    nombre = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    telefono = models.IntegerField()
    provincia = models.ForeignKey(provincia, on_delete=models.CASCADE)

    def __str__(self):
        return self.provincia.nombre

    def get_absolute_url(self):
        return reverse('proveedor-detail', kwargs={'pk':self.pk})