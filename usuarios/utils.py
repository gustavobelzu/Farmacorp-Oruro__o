# usuarios/models.py
from django.db import models
from empleados.models import Empleado
from django.contrib.auth.hashers import make_password, check_password
from datetime import date


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # almacenar hashed
    fecha_creacion = models.DateField(auto_now_add=True)
    ci_empleado = models.ForeignKey(
        Empleado,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    # ======================
    # MÉTODOS DE USUARIO
    # ======================
    def set_password(self, raw_password):
        """Hashea y guarda la contraseña."""
        self.password = make_password(raw_password)
        self.save()
        return "✅ Contraseña guardada."

    def check_password(self, raw_password):
        """Verifica la contraseña ingresada."""
        return check_password(raw_password, self.password)

    def registra_empleados(self, empleados):
        """
        Asocia empleados a este usuario.
        `empleados` puede ser una lista de instancias Empleado.
        """
        registrados = []
        for emp in empleados:
            self.ci_empleado = emp
            self.save()
            registrados.append(emp.nombre)
        return f"Empleado(s) registrados para usuario {self.username}: {', '.join(registrados)}"

    def valida_empleados(self):
        """
        Valida que el empleado asociado exista y esté activo.
        """
        if self.ci_empleado is None:
            return f"❌ Usuario {self.username} no tiene empleado asignado."
        if self.ci_empleado.estado != "activo":
            return f"⚠️ El empleado {self.ci_empleado.nombre} no está activo."
        return f"✅ Empleado {self.ci_empleado.nombre} válido para el usuario {self.username}."

    def __str__(self):
        return self.username
