from django.db import models
from empleados.models import EncargadoAlmacen  # o quien sea responsable del inventario

class Inventario(models.Model):
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=50)
    fecha_actualizacion = models.DateField()
    stock_minimo = models.IntegerField()
    encargado = models.ForeignKey(EncargadoAlmacen, on_delete=models.CASCADE)
