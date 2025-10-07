from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Agrega rutas para cada módulo (puedes crear vistas vacías por ahora)
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
