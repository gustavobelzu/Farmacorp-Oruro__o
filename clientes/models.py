# clientes/models.py
from django.db import models
from empleados.models import Empleado  # Para la relación con Empleado

class Cliente(models.Model):
    ci_cliente = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    ci_empleado = models.ForeignKey(
        Empleado,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.nombre} ({self.ci_cliente})"
