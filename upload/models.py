
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils import timezone


# Create your models here.

OPCIONES_TARJETA = (
    ('T1', 'MODULO DOMOTICO'),
    ('T2', 'MODULO SENSOR TEMPERATURA'),
    ('T3', 'MODULO IMPRESORA 3D'),
    ('T4', 'ESP32 - 4'),
    ('T5', 'ESP32 - 5'),
    ('T6', 'ESP32 - 6'),
    ('T7', 'ESP32 - 7'),
    ('T8', 'ESP32 - 8'),
    ('T9', 'ESP32 - 9'),
    ('T10', 'ESP32 -10'),
    )

class Archivo(models.Model):

    tarjeta = models.CharField(max_length=15, choices=OPCIONES_TARJETA, default='ESP32 - 1')
    archivo = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['bin'])])
    fecha = models.DateTimeField(auto_now=True) 
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
        

    def __str__(self):
         return '%s %s %s' % (self.tarjeta, self.archivo, self.fecha)

    def delete(self, *args, **kwargs):
        self.archivo.delete()
        super().delete(*args, **kwargs)
