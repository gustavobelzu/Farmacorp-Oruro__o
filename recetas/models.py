# recetas/models.py
from django.db import models
from clientes.models import Cliente

class Receta(models.Model):
    id_receta = models.CharField(max_length=50, primary_key=True)
    fecha_emision = models.DateField()
    matricula_medico = models.CharField(max_length=50)
    medicamento = models.CharField(max_length=200)
    cantidad = models.PositiveIntegerField()
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='recetas'
    )

    def __str__(self):
        return f"Receta {self.id_receta} - {self.cliente.nombre}"

class DetalleReceta(models.Model):
    receta = models.ForeignKey(
        Receta,
        on_delete=models.CASCADE,
        related_name='detalles'
    )
    dosis = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=100)
    duracion = models.CharField(max_length=100)
    instrucciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Detalle de {self.receta.id_receta}"
