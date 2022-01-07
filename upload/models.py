from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Usuarios(models.Model):
    usuario = models.CharField(max_length=100)
    clave = models.CharField(max_length=15)
    



    
