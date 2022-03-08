import os
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage, Storage
from django.contrib.auth.decorators import login_required

from .models import Archivo
from .forms import  ArchivoForm, SignUpForm

# Create your views here.

def home(request):
    return render (request, 'home.html')

def secretpage (request):
    archivo = Archivo.objects.values_list('archivo', flat=True).last()
    tarjeta = Archivo.objects.values_list('tarjeta', flat=True).last()
    return render (request, 'secretpage.html', {'archivo': archivo, 'tarjeta': tarjeta})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Usuario {username} creado')
            return redirect('home')
    else:
        form = SignUpForm()
    return render (request, 'registration/signup.html', {'register_form' : form})

#@login_required
def archivos(request):
    user_log = request.user.id
    archivos = Archivo.objects.filter(usuario = user_log).order_by('-fecha')
    return render(request, 'archivos.html', {'archivos':archivos})

#@login_required
def borrarArchivos(request, pk):
    if request.method == 'POST':
        archivo = Archivo.objects.get(pk=pk)
        archivo.delete()
    return redirect('archivos')

#@login_required
def cargar(request):
    
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():  
            form.save(request.user)
            return JsonResponse({'message':'Archivo subido correctamente'})
    else:
        form = ArchivoForm()
    return render(request, 'cargar.html', {'form':form})

def contacto(request):
    return render(request, 'contacto.html')
