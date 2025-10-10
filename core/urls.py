from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('/usuarios/login/')),  # Redirige "/" al login de usuarios
    path('', lambda request: redirect('/farmacia/login/')),  # Redirige "/" a "/farmacia/login/"
    path('farmacia/', include('farmacia.urls')),
    path('usuarios/', include('usuarios.urls')),  # 👈 importante
    path('productos/', include('productos.urls')),


]
