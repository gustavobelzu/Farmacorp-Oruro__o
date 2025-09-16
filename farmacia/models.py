from django.db import models


class Farmacia(models.Model):
    direccion = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

class Sucursal(models.Model):
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    farmacia = models.ForeignKey(Farmacia, on_delete=models.CASCADE, related_name='sucursales')
