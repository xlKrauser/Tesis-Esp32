from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.utils import timezone

# Create your models here.

OPCIONES_TARJETA = (
    ('T1', 'ESP32 - 1'),
    ('T2', 'ESP32 - 2'),
    ('T3', 'ESP32 - 3'),
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
    archivo = models.FileField()
    fecha = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s %s' % (self.tarjeta, self.archivo, self.fecha)
