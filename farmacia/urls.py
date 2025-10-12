from django.urls import path
from . import views

app_name = 'farmacia'

urlpatterns = [
    # Dashboard principal
    path('', views.dashboard, name='dashboard'),
    path('', views.listar_farmacias, name='listar_farmacias'),
    path('crear/', views.crear_farmacia, name='crear_farmacia'),
    path('editar/<int:pk>/', views.editar_farmacia, name='editar_farmacia'),
    path('eliminar/<int:pk>/', views.eliminar_farmacia, name='eliminar_farmacia'),
    path('verificar/<str:nombre>/', views.verificar_farmacia, name='verificar_farmacia'),
    # Vistas de farmacia
    path('farmacia/', views.farmacia_view, name='farmacia'),
    path('usuario/', views.usuario_view, name='usuario'),
    path('sucursal/', views.sucursal_view, name='sucursal'),
    path('empleado/', views.empleado_view, name='empleado'),
    path('proveedor/', views.proveedor_view, name='proveedor'),
    path('reporte/', views.reporte_view, name='reporte'),
    path('cliente/', views.cliente_view, name='cliente'),
    path('venta/', views.venta_view, name='venta'),
    path('receta/', views.receta_view, name='receta'),
    path('producto/', views.producto_view, name='producto'),
    path('alerta/', views.alerta_view, name='alerta'),
    path('inventario/', views.inventario_view, name='inventario'),
    path('almacen/', views.almacen_view, name='almacen'),
]


