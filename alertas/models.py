# alertas/models.py
from django.db import models
from inventarios.models import Inventario

class Alerta(models.Model):
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_alerta = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    inventario = models.ForeignKey(
        Inventario,
        on_delete=models.CASCADE,
        related_name='alertas',
        null=True,  # permite que la alerta exista aunque no haya inventario
        blank=True
    )

    def __str__(self):
        return f"Alerta {self.id} - Tipo: {self.tipo}"
