# proveedores/models.py
from django.db import models
from inventarios.models import Inventario

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

    def __str__(self):
        return self.nombre
