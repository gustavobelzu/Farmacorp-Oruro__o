# proveedores/models.py
from django.db import models
from inventarios.models import Inventario
from datetime import date


class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True)
    inventario = models.ForeignKey(
        Inventario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='proveedores'
    )

    # ======================
    # MÉTODOS DEL PROVEEDOR
    # ======================
    def gestionar_pedido(self, producto, cantidad):
        """Registra un pedido de productos al proveedor."""
        return f"Proveedor {self.nombre} recibió un pedido de {cantidad} unidades de {producto}."

    def gestionar_proveedor(self, accion):
        """Gestiona al proveedor (ej: registrar, actualizar, evaluar, eliminar)."""
        return f"Proveedor {self.nombre} gestionado con la acción: {accion}."

    def gestionar_catalogo(self, productos):
        """Muestra el catálogo de productos ofrecidos por el proveedor."""
        lista_productos = ', '.join(productos) if productos else "Sin productos"
        return f"Proveedor {self.nombre} tiene en catálogo: {lista_productos}."

    def __str__(self):
        return self.nombre
