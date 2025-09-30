from django.db import models
from clientes.models import Cliente
from proveedores.models import Proveedor


class Receta(models.Model):
    fecha = models.DateField()
    numero = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Receta {self.numero} - {self.fecha}"
