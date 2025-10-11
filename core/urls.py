from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login')),  # Redirige al login
    path('clientes/', include('clientes.urls')),  # ✅ Aquí usamos /clientes/
    path('farmacia/', include('farmacia.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('productos/', include('productos.urls')),
]

