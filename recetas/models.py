# recetas/models.py
from django.db import models
from clientes.models import Cliente
from datetime import date


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

    # ======================
    # MÉTODOS DE LA RECETA
    # ======================
    def validar_receta(self):
        """Valida que la receta tenga datos correctos."""
        if not self.matricula_medico:
            return "❌ Error: La receta no tiene matrícula del médico."
        if self.fecha_emision > date.today():
            return "❌ Error: La fecha de emisión no puede ser futura."
        if self.cantidad <= 0:
            return "❌ Error: La cantidad debe ser mayor a 0."
        if not self.cliente:
            return "❌ Error: La receta no tiene cliente asignado."
        return "✅ Receta válida."

    def asociar_medicamento(self, nuevo_medicamento, nueva_cantidad):
        """Asocia o actualiza un medicamento en la receta."""
        self.medicamento = nuevo_medicamento
        self.cantidad = nueva_cantidad
        self.save()
        return f"💊 Medicamento {nuevo_medicamento} asociado con cantidad {nueva_cantidad}."

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
