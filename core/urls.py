from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    # ✅ Redirige "/" al login de usuarios
    path('', lambda request: redirect('login')),  # usa el name de la url
    path('farmacia/', include('farmacia.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('productos/', include('productos.urls')),
    path('clientes/', include('clientes.urls')),


]


