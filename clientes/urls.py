from django.urls import path
from . import views

app_name = 'clientes'  # ← importante para el namespace

urlpatterns = [
    path('', views.listar_clientes, name='listar_clientes'),
    path('crear/', views.crear_cliente, name='crear_cliente'),
    path('editar/<str:ci_cliente>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar/<str:ci_cliente>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('verificar/<str:ci>/', views.verificar_cliente, name='verificar_cliente'),
]
