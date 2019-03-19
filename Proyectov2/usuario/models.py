from django.db import models

class tipoUsuario(models.Model):
    nombre = models.CharField(max_length=15)

class usuario(models.Model):
    nombre = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    correoElectronico = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    tipousuario = models.ForeignKey(tipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre