from django.urls import path
from . import views

app_name = 'empleados'

urlpatterns = [
    path('', views.listar_empleados, name='listar_empleados'),
    path('crear/', views.crear_empleado, name='crear_empleado'),
    path('editar/<str:ci>/', views.editar_empleado, name='editar_empleado'),
    path('eliminar/<str:ci>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('verificar/<str:ci>/', views.verificar_empleado, name='verificar_empleado'),
    path('verificar_matricula/<str:matricula>/', views.verificar_matricula, name='verificar_matricula'),

]
