from django.db import models

class Sucursal(models.Model):
    nombre = models.CharField(max_length=255)
    departamento = models.CharField(max_length=100)
    nit = models.CharField(max_length=50)
    email = models.EmailField()
    direccion = models.CharField(max_length=255)
    horario = models.CharField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)  # equivalente a DATE en SQL

    def __str__(self):
        return self.nombre


class Farmacia(models.Model):
    nombre_farmacia = models.CharField(max_length=255)
    razonLegal = models.CharField(max_length=255)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='farmacias')

    def __str__(self):
        return self.nombre_farmacia
