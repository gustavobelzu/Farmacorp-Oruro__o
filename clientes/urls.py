# clientes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_clientes, name='listar_clientes'),  # <-- Nombre de la ruta
    path('registrar/', views.registrar_cliente, name='registrar_cliente'),
    path('editar/<str:ci_cliente>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar/<str:ci_cliente>/', views.eliminar_cliente, name='eliminar_cliente'),
]
