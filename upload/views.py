
from distutils.command.install_data import install_data
import os
from sre_parse import State
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage, Storage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import Archivo, Profile
from .forms import  ArchivoForm, SignUpForm, ProfileUpdate

# Create your views here.

User = get_user_model()

def home(request):
    return render (request, 'home.html')


@login_required
def profileUpload(request):
    user = request.user.id
    profile = Profile.objects.get(user__id = user)
    user_basic_info = User.objects.get(id=user)
    if request.method == 'POST':
        form = ProfileUpdate(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')

            profile.avatar = form.cleaned_data.get('avatar')
            profile.bio = form.cleaned_data.get('bio')
            profile.save()
            user_basic_info.save()
            return redirect('inicio')
    else:
        form = ProfileUpdate(instance=profile)
    
    return render(request, 'edit_profile.html', {'form': form})
    

@login_required
def inicio(request):
    estados = Archivo.objects.filter(estado=True)
    return render(request, 'inicio.html', {"estados": estados})

@login_required
def cambiarEstado(request, tarjeta):
    if request.method == 'POST':
        cambioEstado = Archivo.objects.filter(tarjeta = tarjeta).update(estado = False)
        print(cambioEstado)
        
    return redirect('inicio')


def secretpage (request):
    archivo = Archivo.objects.values_list('archivo', flat=True).last()
    tarjeta = Archivo.objects.values_list('tarjeta', flat=True).last()
    return render (request, 'secretpage.html', {'archivo': archivo, 'tarjeta':tarjeta})


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

@login_required
def archivos(request):
    user_log = request.user.id
    archivos = Archivo.objects.filter(usuario = user_log).order_by('-fecha')
    return render(request, 'archivos.html', {'archivos':archivos})

@login_required
def borrarArchivos(request, pk):
    if request.method == 'POST':
        archivo = Archivo.objects.get(pk=pk)
        print(archivo)
        archivo.delete()
    return redirect('archivos')

@login_required
def cargar(request):  
    disabled_choices = Archivo.objects.filter(estado=True).values_list('tarjeta', flat=True)
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():  
            form.save(request.user)
            return JsonResponse({'message':'Archivo subido correctamente'})
    else:
        form = ArchivoForm(disabled_choices=disabled_choices)
    return render(request, 'cargar.html', {'form':form})

def contacto(request):
    return render(request, 'contacto.html')
