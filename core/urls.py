
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include

"""
 urls de la app Usuarios
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('SSO.urls')),
    path('accounts/',include('allauth.urls')), #path del sso
    path('usuarios/',include('Usuarios.urls')),#path de usuarios
]
