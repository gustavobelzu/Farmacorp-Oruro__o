from django.db import models
from clientes.models import Cliente
from proveedores.models import Medico
from productos.models import Medicamento

class Receta(models.Model):
    fecha = models.DateField()
    numero = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)

    def __str__(self):
        return f"Receta {self.numero} - {self.fecha}"
