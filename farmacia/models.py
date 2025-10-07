# farmacia/models.py
from django.db import models

class Sucursal(models.Model):
    nombre = models.CharField(max_length=200)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    nit = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    horario = models.CharField(max_length=100, blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)

    # ======================
    # MÉTODOS DE SUCURSAL
    # ======================
    def gestionar_farmacia(self, farmacia):
        """Gestiona una farmacia asociada a esta sucursal."""
        return f"Sucursal {self.nombre} gestiona la farmacia {farmacia.nombre_farmacia}."

    def registrar_horario(self, nuevo_horario):
        """Actualiza el horario de atención de la sucursal."""
        self.horario = nuevo_horario
        self.save()
        return f"Sucursal {self.nombre} actualizó su horario a: {self.horario}."

    def consultar_inventario(self, inventarios):
        """Consulta inventario(s) de las farmacias asociadas."""
        return f"Sucursal {self.nombre} consultó {len(inventarios)} registros de inventario."

    def __str__(self):
        return self.nombre


class Farmacia(models.Model):
    nombre_farmacia = models.CharField(max_length=200)
    razon_legal = models.CharField(max_length=200, blank=True, null=True)
    id_sucursal = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE,
        related_name='farmacias'
    )

    # ======================
    # MÉTODOS DE FARMACIA
    # ======================
    def gestiona_sucursal(self):
        """Indica la sucursal a la que pertenece esta farmacia."""
        return f"La farmacia {self.nombre_farmacia} pertenece a la sucursal {self.id_sucursal.nombre}."

    def gestiona_producto(self, producto, accion):
        """Gestiona un producto en la farmacia (ej: agregar, actualizar, eliminar)."""
        return f"Farmacia {self.nombre_farmacia} realizó la acción '{accion}' sobre el producto {producto}."

    def gestiona_proveedor(self, proveedor, accion):
        """Gestiona proveedores asociados (ej: registrar, evaluar, eliminar)."""
        return f"Farmacia {self.nombre_farmacia} realizó la acción '{accion}' con el proveedor {proveedor}."

    def __str__(self):
        return self.nombre_farmacia
