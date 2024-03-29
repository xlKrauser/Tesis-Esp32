"""Subir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse_lazy

from upload.models import Archivo
from upload.forms import MyPasswordChangeForm, MySetPasswordForm
from upload import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name = 'home'),
    path('signup/', views.signup, name = 'signup'),
    path('', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name='home' ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('change_password/', auth_views.PasswordChangeView.as_view(
        template_name = 'registration/password_change.html', form_class = MyPasswordChangeForm), name='password_change'),
    path('change_password/done/', auth_views.PasswordChangeDoneView.as_view(), name = 'password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name = 'password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(form_class = MySetPasswordForm), name = 'password_reset_confirm'),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
    path('cargar/', views.cargar, name = 'cargar'),
    path('lectura/', views.lectura, name = 'lectura'),
    path('archivos/', views.archivos, name = 'archivos'),
    path('archivos/<int:pk>', views.borrarArchivos, name = 'borrarArchivos'),
    # path('contacto/', views.contacto, name = 'contacto'),
    path('secretpage/', views.secretpage, name = 'secretpage'),
    path('inicio/', views.inicio, name='inicio'),
    path('inicio/<tarjeta>', views.cambiarEstado, name='cambiarEstado'),
    path('editar_perfil/', views.profileUpload, name="editar_perfil"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)