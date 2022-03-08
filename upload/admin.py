from django.contrib import admin

from .models import Archivo
from .forms import ArchivoForm

# Register your models here.
class ArchivosAdmin(admin.ModelAdmin):
    list_display = ('tarjeta','archivo','fecha')
    search_fields = ('archivo','nombre',)
    list_filter = ('fecha',)

admin.site.register(Archivo, ArchivosAdmin)
