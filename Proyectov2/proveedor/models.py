from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.urls import reverse
import datetime


class provincia(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class proveedor(models.Model):
    nombre = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    telefono = models.IntegerField()
    provincia = models.ForeignKey(provincia, on_delete=models.CASCADE)
    calificacion = models.FloatField(default=0.0)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('proveedor-detail', kwargs={'id':self.pk})

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

class Comentario(models.Model):
    Proveedor = models.ForeignKey(proveedor, on_delete = models.CASCADE, related_name="comments")
    Usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="autor")
    fecha = models.DateField(("Date"), default=datetime.date.today)
    texto = models.TextField(max_length=150)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.texto


class Rating(models.Model):
    Proveedor = models.ForeignKey(proveedor, on_delete=models.CASCADE, related_name='calif')
    Usuario =  models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
    promedio = models.IntegerField()


class ratings_prov(models.Model):
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, related_name="ratingComment")
    tipo = models.CharField(max_length=25)
    calificacion = models.IntegerField()

class movimientos_pagina(models.Model):
    UsuarioMovimiento = models.ForeignKey(User, on_delete = models.PROTECT)
    TipoMovimiento = models.CharField(max_length=45)
    FechaMovimiento = models.DateField()
    HoraMovimiento = models.TimeField()

    def __str__(self):
        return self.movimentos_pagina.UsuarioMovimiento.username
