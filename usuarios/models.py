from django.db import models
from empleados.models import Empleado  # FK al modelo Empleado

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # puedes usar hashing después
    fecha_creacion = models.DateField(auto_now_add=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username
