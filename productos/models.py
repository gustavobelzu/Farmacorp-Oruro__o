from django.db import models

class Proveedor(models.Model):
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

class Producto(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock_min = models.IntegerField()
    stock_max = models.IntegerField()
    proveedores = models.ManyToManyField(Proveedor)

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    composicion = models.TextField()
    indicaciones = models.TextField()
    via_administracion = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

class Alerta(models.Model):
    tipo = models.CharField(max_length=50)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    activada = models.BooleanField(default=False)
