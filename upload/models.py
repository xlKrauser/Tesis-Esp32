from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.

class Usuarios(models.Model):
    nombre =  models.CharField(max_length=100)
    tamaño = models.IntegerField(max_length=20)
    fecha =  models.DateTimeField('publicacion')