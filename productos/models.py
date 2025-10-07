# productos/models.py
from django.db import models
from inventarios.models import Inventario
from clientes.models import Cliente
from datetime import date


class Producto(models.Model):
    codigo_barra = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    precio_unitario = models.FloatField()
    stock = models.IntegerField()
    fecha_vencimiento = models.DateField(blank=True, null=True)
    iva = models.CharField(max_length=10, blank=True, null=True)
    id_inventario = models.ForeignKey(
        Inventario,
        on_delete=models.CASCADE,
        related_name='productos'
    )
    ci_cliente = models.ForeignKey(
        Cliente,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='productos'
    )

    # ======================
    # MÉTODOS DEL PRODUCTO
    # ======================

    def gestionar_producto(self, accion):
        """Gestiona el producto (ej: registrar, actualizar, eliminar)."""
        return f"Producto {self.nombre} fue gestionado con la acción: {accion}."

    def calcular_precio_final(self):
        """Calcula el precio final con IVA (si está definido)."""
        try:
            iva_valor = float(self.iva.replace('%', '')) / 100 if self.iva else 0
        except ValueError:
            iva_valor = 0
        precio_final = self.precio_unitario * (1 + iva_valor)
        return round(precio_final, 2)

    def notificar_vencimiento(self):
        """Notifica si el producto está vencido o próximo a vencer."""
        if not self.fecha_vencimiento:
            return f"Producto {self.nombre} no tiene fecha de vencimiento registrada."
        
        hoy = date.today()
        dias_restantes = (self.fecha_vencimiento - hoy).days

        if dias_restantes < 0:
            return f"⚠️ Producto {self.nombre} está vencido (venció el {self.fecha_vencimiento})."
        elif dias_restantes <= 30:
            return f"⚠️ Producto {self.nombre} está próximo a vencer en {dias_restantes} días."
        else:
            return f"Producto {self.nombre} vence en {dias_restantes} días."

    def __str__(self):
        return self.nombre
