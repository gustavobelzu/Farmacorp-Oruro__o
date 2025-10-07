# clientes/models.py
from django.db import models
from empleados.models import Empleado

class Cliente(models.Model):
    ci_cliente = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    ci_empleado = models.ForeignKey(
        Empleado,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.nombre} ({self.ci_cliente})"

    # ======================
    # MÉTODOS DEL CLIENTE
    # ======================

    def realizar_compra(self, productos):
        """
        Simula la acción de realizar una compra.
        productos: lista de diccionarios con {producto, cantidad}.
        """
        return f"Cliente {self.nombre} realizó la compra de {len(productos)} productos."

    def consultar_receta(self, receta_id):
        """
        Simula la consulta de una receta médica por su ID.
        """
        return f"Cliente {self.nombre} consulta la receta con ID {receta_id}."

    def solicitar_factura(self, compra_id):
        """
        Simula la solicitud de factura para una compra realizada.
        """
        return f"Cliente {self.nombre} solicita factura de la compra {compra_id}."
