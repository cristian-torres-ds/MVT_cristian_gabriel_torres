from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    relacion = models.CharField(max_length=30)
    telefono = models.IntegerField()
    email = models.EmailField()
    nacimiento = models.DateField()

class Amigo(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField()
    nacimiento = models.DateField()

