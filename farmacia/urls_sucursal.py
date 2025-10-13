from django.urls import path
from . import views_sucursal
from . import views  # para farmacias

app_name = 'sucursal'

urlpatterns = [
    path('', views_sucursal.listar_sucursal, name='listar_sucursal'),
    path('crear/', views_sucursal.crear_sucursal, name='crear_sucursal'),
    path('editar/<int:id>/', views_sucursal.editar_sucursal, name='editar_sucursal'),
    path('eliminar/<int:id>/', views_sucursal.eliminar_sucursal, name='eliminar_sucursal'),
    
    # Verificaciones
    path('verificar/<int:id>/', views_sucursal.verificar_sucursal, name='verificar_sucursal'),  # para editar/eliminar
    path('verificar_nit/<str:nit>/', views_sucursal.verificar_nit, name='verificar_nit'),       # para crear

    
]
