from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class provincia(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class proveedor(models.Model):
    nombre = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    telefono = models.IntegerField()
    provincia = models.ForeignKey(provincia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('proveedor-detail', kwargs={'pk':self.pk})

class reporteProveedor(models.Model):
    Proveedor = models.ForeignKey(proveedor, on_delete = models.PROTECT)
    Usuario = models.ForeignKey(User, on_delete = models.PROTECT)

    def __str__(self):
        return self.Proveedor.nombre

class agregadoFavoritosProveedor(models.Model):
    Proveedor = models.ForeignKey(proveedor, on_delete = models.PROTECT)
    Usuario = models.ForeignKey(User, on_delete = models.PROTECT)

    def __str__(self):
        return self.Usuario.username

class movimientos_pagina(models.Model):
    UsuarioMovimiento = models.ForeignKey(User, on_delete = models.PROTECT)
    TipoMovimiento = models.CharField(max_length=45)
    FechaMovimiento = models.DateField()
    HoraMovimiento = models.TimeField()

    def __str__(self):
        return self.movimentos_pagina.UsuarioMovimiento.username
