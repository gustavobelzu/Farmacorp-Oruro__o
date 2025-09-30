# inventarios/models.py
from django.db import models
from empleados.models import EncargadoInventario

class Inventario(models.Model):
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=50, blank=True, null=True)
    fecha_actualizacion = models.DateField(blank=True, null=True)
    stock_minimo = models.IntegerField()
    ci_encargado = models.ForeignKey(
        EncargadoInventario,
        on_delete=models.CASCADE,
        related_name='inventarios'
    )

    def __str__(self):
        return f"Inventario {self.id} - Encargado: {self.ci_encargado.ci}"
