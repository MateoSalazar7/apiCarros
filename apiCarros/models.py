from django.db import models

# Create your models here.

class Carro(models.Model):
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    año = models.PositiveIntegerField(default=0)
    color = models.DateTimeField(auto_now_add=True)
    tipo_combustible = models.CharField(max_length=200)
    descripcion = models.TextField()
    puertas = models.PositiveIntegerField(default=0)
    transmision = models.CharField(max_length=200)
    motor = models.PositiveIntegerField(default=0)
    tipo_carroceria = models.CharField(max_length=200)
