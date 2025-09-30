# empleados/models.py (o en un archivo separado si quieres, ej. usuarios/models.py)
from django.db import models
from empleados.models import Empleado  # importa la tabla Empleado

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # puedes usar hashing con Django
    fecha_creacion = models.DateField(auto_now_add=True)
    ci_empleado = models.ForeignKey(
        Empleado,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username
