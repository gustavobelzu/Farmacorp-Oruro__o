from django.db import models
from farmacia.models import Farmacia

class Empleado(models.Model):
    ci = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    salario = models.FloatField(null=True, blank=True)
    cargo = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    estado = models.CharField(max_length=20, null=True, blank=True)
    turno = models.CharField(max_length=20, null=True, blank=True)
    fechaIngreso = models.DateField()
    fechaSalida = models.DateField(null=True, blank=True)
    farmacia = models.ForeignKey(Farmacia, on_delete=models.SET_NULL, null=True, blank=True, related_name='empleados')

    def __str__(self):
        return f"{self.nombre} ({self.ci})"


class Farmaceutico(models.Model):
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=100, null=True, blank=True)

    def validar_receta(self, receta):
        # lógica de validación
        return True


class Administrador(models.Model):
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE)


class EncargadoInventario(models.Model):
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE)
