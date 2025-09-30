from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    direccion = models.CharField(max_length=255)
    estado = models.CharField(max_length=50, null=True, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)
