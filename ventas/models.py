# ventas/models.py
from django.db import models
from clientes.models import Cliente

class Venta(models.Model):
    factura = models.BooleanField(default=False)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='ventas'
    )

    def __str__(self):
        return f"Venta {self.id} - Cliente: {self.cliente.nombre}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(
        Venta,
        on_delete=models.CASCADE,
        related_name='detalles'
    )
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    descuento = models.BooleanField(default=False)

    def __str__(self):
        return f"Detalle de Venta {self.venta.id}"
