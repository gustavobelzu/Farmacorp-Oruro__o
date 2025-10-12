from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
path('', lambda request: redirect('usuarios:login')),  # Redirige al login
    path('clientes/', include('clientes.urls', namespace='clientes')),  # ← namespace
    path('farmacia/', include('farmacia.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('productos/', include('productos.urls')),
    path('empleados/', include('empleados.urls', namespace='empleados')),  # ← Agregado para empleados

]

