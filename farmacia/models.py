# farmacia/models.py
from django.db import models

class Sucursal(models.Model):
    nombre = models.CharField(max_length=200)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    nit = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    horario = models.CharField(max_length=100, blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Farmacia(models.Model):
    nombre_farmacia = models.CharField(max_length=200)
    razon_legal = models.CharField(max_length=200, blank=True, null=True)
    id_sucursal = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE,
        related_name='farmacias'
    )

    def __str__(self):
        return self.nombre_farmacia
