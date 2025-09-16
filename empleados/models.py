from django.db import models
from farmacia.models import Sucursal

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    rol = models.CharField(max_length=50)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)

class Farmaceutico(models.Model):
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=50)
    def validar_receta(self, receta):
        # lógica de validación
        return True

class Administrador(models.Model):
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE)

class EncargadoAlmacen(models.Model):
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE)
