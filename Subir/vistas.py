from django.http import HttpResponse, HttpResponseRedirect
from django.http.request import HttpRequest
from django.views.generic import TemplateView
from django.shortcuts import render, redirect


def cargar(request):
    if request.method =='POST':
        subir_archivo = request.FILES['archivo']
        print(subir_archivo.name)
        print(subir_archivo.size)
    return render(request, 'cargar.html')