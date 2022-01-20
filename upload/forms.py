from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import Archivo


class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo        
        fields = ('tarjeta', 'archivo')

class SignUpForm(forms.Form):
    username = forms.CharField(label='Usuario' ,min_length=6, max_length=20)
    email = forms.EmailField(label='Correo Electronico', required=True, max_length=40)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirme su contraseña', widget=forms.PasswordInput())

    """def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-3 mb-0 input'),
                Column('email', css_class='form-group col-md-3 mb-0 input'),
                Column('password1', css_class='form-group col-md-3 mb-0 input'),
                Column('password2', css_class='form-group col-md-3 mb-0 input'),
                css_class='form-row'
            )
        )"""

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
            self.cleaned_data['password1']
        )
        return user
        
        

    




