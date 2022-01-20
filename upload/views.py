
from django.shortcuts import render, redirect
from .forms import  ArchivoForm, SignUpForm
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render (request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()

    return render (request, 'registration/signup.html', {'register_form' : form})

def login(request):
    return render (request, 'registration/login.html')

def archivo(request):
    return render(request, 'archivo.html')

def cargar(request):
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    else:
        form = ArchivoForm()
    return render(request, 'cargar.html', {'form' : form})

"""def cargar(request):
    if request.method =='POST':
        subir_archivo = request.FILES['archivo']
        fs = FileSystemStorage()
        fs.save(subir_archivo.name, subir_archivo)
    return render(request, 'cargar.html')"""

