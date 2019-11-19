from django.db import models

class Tour(models.Model):
    #id = models.IntegerField(primary_key=True)
    lugar = models.CharField(max_length = 200)
    descripcion = models.CharField(max_length=1000)
    fecha = fecha = models.DateTimeField(auto_now_add= False, auto_now= False)
    cupos = models.IntegerField(null=True)
    imagen = models.CharField(max_length = 200)

    def __str__(self):
        return self.lugar

class Turista(models.Model):
    identificacion = models.IntegerField()
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    idioma = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre


class Guia(models.Model):
    identificacion = models.IntegerField()
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    idioma = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

