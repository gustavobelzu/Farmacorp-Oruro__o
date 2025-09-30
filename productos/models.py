# productos/models.py
from django.db import models
from inventarios.models import Inventario
from clientes.models import Cliente

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

    def __str__(self):
        return self.nombre
