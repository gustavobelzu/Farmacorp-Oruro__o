from django.db import models
from inventarios.models import Inventario

class Alerta(models.Model):
    id_alerta = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_alerta = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='Pendiente')
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE, related_name='alertas')

    def __str__(self):
        return f"{self.tipo} - {self.estado}"
