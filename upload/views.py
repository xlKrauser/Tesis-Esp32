<<<<<<< HEAD
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

# Create your views here.

def cargar(request):
    if request.method =='POST':
        subir_archivo = request.FILES['archivo']
        fs = FileSystemStorage()
        fs.save(subir_archivo.name, subir_archivo)
    return render(request, 'cargar.html')

