from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_clientes, name='listar_clientes'),  # /clientes/
    path('registrar/', views.registrar_cliente, name='registrar_cliente'),  # /clientes/registrar/
    path('editar/<str:ci_cliente>/', views.editar_cliente, name='editar_cliente'),  # /clientes/editar/CI
    path('eliminar/<str:ci_cliente>/', views.eliminar_cliente, name='eliminar_cliente'),  # /clientes/eliminar/CI
]
