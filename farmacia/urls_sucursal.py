# farmacia/urls_sucursal.py
from django.urls import path
from . import view_sucursal  # Importa tu view_sucursal.py

urlpatterns = [
    path('', view_sucursal.listar_sucursales, name='sucursal_listar'),
    path('crear/', view_sucursal.crear_sucursal, name='crear_sucursal'),
    path('editar/<int:pk>/', view_sucursal.editar_sucursal, name='editar_sucursal'),
    path('eliminar/<int:pk>/', view_sucursal.eliminar_sucursal, name='eliminar_sucursal'),
    path('verificar/', view_sucursal.verificar_sucursal, name='verificar_sucursal'),
]
