# inventarios/models.py
from django.db import models
from empleados.models import EncargadoInventario


class Almacen(models.Model):
    categoria = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    fecha_ingreso = models.DateField(blank=True, null=True)
    fecha_salida = models.DateField(blank=True, null=True)

    # ======================
    # MÉTODOS DEL ALMACÉN
    # ======================
    def verificar_disponibilidad(self):
        """Verifica si el almacén tiene inventarios registrados."""
        inventarios_count = self.inventarios.count()
        return f"El almacén {self.categoria} ({self.ubicacion}) tiene {inventarios_count} inventarios."

    def gestionar_almacen(self, accion):
        """Gestiona el almacén (ej: apertura, cierre, reorganización)."""
        return f"Almacén {self.categoria} ({self.ubicacion}) realizó la acción: {accion}."

    def __str__(self):
        return f"Almacén {self.categoria} - {self.ubicacion}"


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
    id_almacen = models.ForeignKey(
        Almacen,
        on_delete=models.CASCADE,
        related_name='inventarios'
    )

    # ======================
    # MÉTODOS DEL INVENTARIO
    # ======================
    def actualiza_cantidad(self, nueva_cantidad):
        """Actualiza la cantidad del inventario."""
        self.cantidad = nueva_cantidad
        self.save()
        return f"Inventario {self.id} actualizado con cantidad: {self.cantidad}."

    def traslada_producto(self, nuevo_almacen):
        """Traslada el inventario a otro almacén."""
        self.id_almacen = nuevo_almacen
        self.save()
        return f"Inventario {self.id} trasladado al almacén {nuevo_almacen.ubicacion}."

    def genera_alerta_stock(self):
        """Genera una alerta si el stock es menor al mínimo."""
        if self.cantidad < self.stock_minimo:
            return f"⚠️ Alerta: Inventario {self.id} bajo en stock (Cantidad: {self.cantidad}, Mínimo: {self.stock_minimo})."
        return f"Inventario {self.id} tiene stock suficiente."

    def verifica_stock(self):
        """Verifica si el stock está por encima o debajo del mínimo."""
        return self.cantidad >= self.stock_minimo

    def __str__(self):
        return f"Inventario {self.id} - Encargado: {self.ci_encargado.empleado.nombre}"
