from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.utils import timezone
import os
from django.conf import settings
from PIL import Image
from django.db.models.signals import post_save

# Create your models here.

def user_directory_path_profile(instance, filename):
    profile_picture_name = 'user/{0}/profile.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)
    
    return profile_picture_name

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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to = user_directory_path_profile, null=True, blank=True)
    bio = models.TextField(null=True, blank=True, max_length=300)
    
    def __str__(self):
        return self.user.username

def created_user_profile(sender, instance, created, **kwargs):
    if  created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(created_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)


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
