# ventas/models.py
from django.db import models
from clientes.models import Cliente
from productos.models import Producto
from inventarios.models import Inventario
from decimal import Decimal

class Venta(models.Model):
    factura = models.BooleanField(default=False)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=50)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='ventas'
    )

    # ======================
    # MÉTODOS DE VENTA
    # ======================
    def calcular_total(self):
        """Calcula el total de la venta sumando todos los subtotales."""
        total = sum(detalle.subtotal for detalle in self.detalles.all())
        self.total = total
        self.save()
        return self.total

    def generar_factura(self):
        """Marca la venta como facturada y devuelve un mensaje."""
        self.factura = True
        self.save()
        return f"Factura generada para la venta {self.id}."

    def actualizar_inventario(self):
        """Resta las cantidades vendidas del inventario de cada producto."""
        for detalle in self.detalles.all():
            producto = detalle.producto  # asumimos que DetalleVenta tendrá un FK a Producto
            if producto.stock >= detalle.cantidad:
                producto.stock -= detalle.cantidad
                producto.save()
            else:
                return f"⚠️ No hay suficiente stock de {producto.nombre}."
        return "Inventario actualizado correctamente."

    def registrar_pago(self, metodo="Efectivo"):
        """Registra el pago de la venta."""
        self.estado = "pagado"
        self.save()
        return f"Pago registrado con método {metodo} para la venta {self.id}."

    def cancelar_pago(self):
        """Cancela el pago de la venta."""
        self.estado = "pendiente"
        self.save()
        return f"Pago cancelado para la venta {self.id}."

    def aplicar_descuento(self, porcentaje):
        """Aplica un descuento sobre el total de la venta."""
        descuento = self.total * Decimal(porcentaje) / 100
        self.total -= descuento
        self.save()
        return f"Descuento del {porcentaje}% aplicado. Total: {self.total}"

    def __str__(self):
        return f"Venta {self.id} - Cliente: {self.cliente.nombre}"


class DetalleVenta(models.Model):
    venta = models.ForeignKey(
        Venta,
        on_delete=models.CASCADE,
        related_name='detalles'
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name='detalle_ventas'
    )
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    descuento = models.BooleanField(default=False)

    def calcular_subtotal(self):
        """Calcula el subtotal de este detalle."""
        self.subtotal = self.precio_unitario * self.cantidad
        self.save()
        return self.subtotal

    def __str__(self):
        return f"Detalle de Venta {self.venta.id} - Producto: {self.producto.nombre}"
