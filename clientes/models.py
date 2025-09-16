from django.db import models

class Cliente(models.Model):
    Ci =models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    def historial_compras(self):
        return self.venta_set.all()

    def historial_recetas(self):
        return self.receta_set.all()
