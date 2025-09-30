from django.db import models

# Create your models here.
from django.db import models
from empleados.models import EncargadoInventario

class Inventarios(models.Model):
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=50)
    fecha_actualizacion = models.DateField(auto_now=True)
    stock_minimo = models.IntegerField()
    encargado = models.ForeignKey(
        EncargadoInventario,
        on_delete=models.CASCADE,  # Si se elimina el encargado, se elimina su inventario
        related_name='inventarios'
    )

    def __str__(self):
        return f"Inventario {self.id} - Encargado: {self.encargado.empleado.nombre}"
