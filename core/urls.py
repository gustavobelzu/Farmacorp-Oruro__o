from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('usuarios:login')),  # Redirige al login
    # 🔹 Redirige raíz al listado de sucursales (por ejemplo)
    path('', lambda request: redirect('listar_sucursal')),

    # 🔹 Módulos
    path('', include('farmacia.urls')),           # rutas para farmacia
    path('', include('farmacia.urls_sucursal')),  # rutas para sucursal    
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('clientes/', include('clientes.urls', namespace='clientes')),  # ← namespace
    path('productos/', include('productos.urls')),
    path('empleados/', include('empleados.urls', namespace='empleados')),  # ← Agregado para empleados

]

