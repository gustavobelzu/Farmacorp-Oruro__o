from django.urls import path
from . import views_sucursal
from . import views  # para funciones de farmacias


urlpatterns = [
    path('', views_sucursal.listar_sucursal, name='listar_sucursal'),
    path('crear/', views_sucursal.crear_sucursal, name='crear_sucursal'),
    path('editar/<int:id>/', views_sucursal.editar_sucursal, name='editar_sucursal'),
    path('eliminar/<int:id>/', views_sucursal.eliminar_sucursal, name='eliminar_sucursal'),
    path('farmacia/<int:id>/', views.listar_farmacia, name='listar_farmacia'),  # ✅ usar views
]
