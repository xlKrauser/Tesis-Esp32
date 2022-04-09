
from cProfile import label
from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from django.forms import ValidationError


from upload.models import Archivo, Profile

class ArchivoForm(forms.ModelForm):

    class Meta:
        model = Archivo        
        fields = ('tarjeta', 'archivo')
    
    def save(self, user):
        obj = super().save(commit=False)
        obj.usuario = user
        obj.save()
        return obj

class SignUpForm(forms.Form):
    username = forms.CharField(label='Usuario' ,min_length=6, max_length=20)
    email = forms.EmailField(label='Correo Electronico', required=True, max_length=40)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(), min_length=6)
    password2 = forms.CharField(label='Confirme su contraseña', widget=forms.PasswordInput(), min_length=6)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError('El nombre de usuario ya existe')
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError('El correo electronico ya esta en uso')
        return email
    
    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('La contraseña no coincide')
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
        )
        return user

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label = "Contraseña anterior", widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'Contraseña anterior'}))
    new_password1 = forms.CharField(label = "Contraseña nueva", widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'Constraseña nueva'}))
    new_password2 = forms.CharField(label = "Confirmar contraseña", widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'Confirme su contraseña'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label = "Contraseña nueva", widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder': 'Contraseña nueva'}))
    new_password2 = forms.CharField(label = "Confirmar contraseña", widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder': 'Confirmar contraseña'}))

    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')

class ProfileUpdate(forms.ModelForm):
    first_name = forms.CharField(label='Nombres', required=True,
        widget = forms.TextInput(attrs={
            'class':'form-control', 'placeholder':'Nombres'
        })
    )
    last_name = forms.CharField(label='Apellidos', required=True,
        widget = forms.TextInput(attrs={
            'class':'form-control', 'placeholder':'Apellidos'
        })
    )
    avatar = forms.ImageField(label='Imagen de perfil', required=False, widget=forms.FileInput)
    bio = forms.CharField(label='Descripcion', required=False, widget=forms.Textarea(attrs={
      'class':'form-control', 'rows':3  
    }))

    class Meta:
        model=Profile
        fields = ('avatar','first_name','last_name', 'bio')
