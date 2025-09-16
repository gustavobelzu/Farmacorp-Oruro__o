from django.db import models
from ventas.models import Venta
from productos.models import Producto

class Reporte(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    ventas = models.ManyToManyField(Venta)
    productos = models.ManyToManyField(Producto)
