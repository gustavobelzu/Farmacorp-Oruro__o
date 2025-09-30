# empleados/models.py
from django.db import models

class Empleado(models.Model):
    ci = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    salario = models.FloatField(blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    turno = models.CharField(max_length=20, blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    fecha_salida = models.DateField(blank=True, null=True)
    id_farmacia = models.ForeignKey(
        'farmacia.Farmacia', 
        on_delete=models.SET_NULL, 
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.nombre} ({self.ci})"


class Farmaceutico(models.Model):
    empleado = models.OneToOneField(
        Empleado,
        on_delete=models.CASCADE,
        primary_key=True
    )
    matricula = models.CharField(max_length=50, blank=True, null=True)
    especialidad = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.empleado.nombre} - {self.especialidad}"


class Administrador(models.Model):
    empleado = models.OneToOneField(
        Empleado,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return self.empleado.nombre


class EncargadoInventario(models.Model):
    empleado = models.OneToOneField(
        Empleado,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return self.empleado.nombre

