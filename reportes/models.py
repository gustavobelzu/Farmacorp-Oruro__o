# empleados/models.py (o en un archivo separado si quieres, ej. reportes/models.py)
from django.db import models
from empleados.models import Empleado  # importa la tabla Empleado

class Reporte(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    fecha_reporte = models.DateField(auto_now_add=True)
    tipo = models.CharField(max_length=100)
    ci_empleado = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Reporte {self.id_reporte} - {self.tipo}"
