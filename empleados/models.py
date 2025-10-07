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

    # ======================
    # MÉTODOS DEL EMPLEADO
    # ======================
    def autentificar(self, username, password):
        """Simula autenticación del empleado en el sistema."""
        return f"Empleado {self.nombre} autenticado con usuario {username}."

    def registrar_asistencia(self, fecha):
        """Marca la asistencia del empleado en una fecha dada."""
        return f"Empleado {self.nombre} registró asistencia el {fecha}."

    def generar_reporte(self, tipo):
        """Genera un reporte asociado al empleado."""
        return f"Empleado {self.nombre} generó un reporte de tipo {tipo}."

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

    # ======================
    # MÉTODOS DEL FARMACÉUTICO
    # ======================
    def validar_receta(self, receta_id):
        """Valida una receta médica."""
        return f"Farmacéutico {self.empleado.nombre} validó la receta {receta_id}."

    def entregar_medicamento(self, medicamento, cantidad):
        """Entrega medicamento al cliente."""
        return f"Farmacéutico {self.empleado.nombre} entregó {cantidad} de {medicamento}."

    def recomendacion_cliente(self, cliente, recomendacion):
        """Brinda una recomendación al cliente."""
        return f"Farmacéutico {self.empleado.nombre} recomendó a {cliente}: {recomendacion}."

    def __str__(self):
        return f"{self.empleado.nombre} - {self.especialidad}"


class Administrador(models.Model):
    empleado = models.OneToOneField(
        Empleado,
        on_delete=models.CASCADE,
        primary_key=True
    )

    # ======================
    # MÉTODOS DEL ADMINISTRADOR
    # ======================
    def gestiona_empleado(self, empleado):
        """Administra un empleado específico."""
        return f"Administrador {self.empleado.nombre} gestiona al empleado {empleado.nombre}."

    def toma_decisiones(self, decision):
        """Simula la toma de una decisión administrativa."""
        return f"Administrador {self.empleado.nombre} tomó la decisión: {decision}."

    def __str__(self):
        return self.empleado.nombre


class EncargadoInventario(models.Model):
    empleado = models.OneToOneField(
        Empleado,
        on_delete=models.CASCADE,
        primary_key=True
    )

    # ======================
    # MÉTODOS DEL ENCARGADO DE INVENTARIO
    # ======================
    def gestionar_inventario(self, accion):
        """Gestiona el inventario (ej: actualizar, revisar, etc.)."""
        return f"Encargado {self.empleado.nombre} realizó la acción: {accion} en el inventario."

    def realizar_pedido(self, producto, cantidad):
        """Realiza un pedido de reabastecimiento."""
        return f"Encargado {self.empleado.nombre} pidió {cantidad} unidades de {producto}."

    def control_stock(self, producto):
        """Verifica el stock de un producto."""
        return f"Encargado {self.empleado.nombre} verificó el stock del producto {producto}."

    def __str__(self):
        return self.empleado.nombre
