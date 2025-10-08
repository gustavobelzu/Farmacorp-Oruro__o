from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='producto_listar'),        # Listar todos los productos
    path('crear/', views.crear_producto, name='crear_producto'),      # Crear nuevo producto
    path('editar/<str:codigo_barra>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<str:codigo_barra>/', views.eliminar_producto, name='eliminar_producto'),
    path('eliminar/<str:codigo_barra>/', views.eliminar_producto, name='eliminar_producto'),

]
