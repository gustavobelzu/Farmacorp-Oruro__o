from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('usuarios:login')),  # Redirige al login
    # 🔹 Redirige raíz al listado de sucursales (por ejemplo)
    # 🔹 Módulos
    path('farmacia/', include('farmacia.urls', namespace='farmacia')),
    path('sucursal/', include('farmacia.urls_sucursal', namespace='sucursal')),
   
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('clientes/', include('clientes.urls', namespace='clientes')),  # ← namespace
    path('productos/', include('productos.urls')),
    path('empleados/', include('empleados.urls', namespace='empleados')),  # ← Agregado para empleados

]

