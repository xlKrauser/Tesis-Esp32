
from cProfile import label
from dataclasses import fields
from email.policy import default
from multiprocessing.sharedctypes import Value
from pyexpat import model
from random import choices
from django import forms
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from django.forms import ValidationError, Select
from upload.models import Archivo, Profile
from django.utils.encoding import force_str
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe


class MySelect(Select):

    def __init__(self, *args, **kwargs):
        self._disabled_choices = []
        super(MySelect, self).__init__(*args, **kwargs)

    @property
    def disabled_choices(self):
        return self._disabled_choices

    @disabled_choices.setter
    def disabled_choices(self, other):
        self._disabled_choices = other

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option_dict = super(MySelect, self).create_option(
            name, value, label, selected, index, subindex=subindex, attrs=attrs
        )
        if value in self.disabled_choices:
            option_dict['attrs']['disabled'] = 'disabled'
        return option_dict
class ArchivoForm(forms.ModelForm):

    class Meta:
        model = Archivo        
        fields = ('tarjeta', 'archivo')

    tarjeta = forms.ChoiceField(widget=MySelect,choices=Archivo.OPCIONES_TARJETA)

    def __init__(self, *args, disabled_choices=None, **kwargs):
        super(ArchivoForm, self).__init__(*args, **kwargs)
        if disabled_choices:
            self.fields['tarjeta'].widget.disabled_choices = disabled_choices

    def save(self, user):
        obj = super().save(commit=False)
        obj.usuario = user
        obj.estado = True
        obj.save()
        return obj

class SignUpForm(forms.Form):
    username = forms.CharField(label='Usuario' ,min_length=6, max_length=20)
    # first_name = forms.CharField(label='Nombres', required=True, max_length=40)
    # last_name = forms.CharField(label='Apellidos', required=True, max_length=60)
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
            # first_name = self.cleaned_data['first_name'],
            # last_name = self.cleaned_data['last_name'],
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
