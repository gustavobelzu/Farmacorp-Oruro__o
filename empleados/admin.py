# empleados/admin.py
from django.contrib import admin
from .models import Empleado, Farmaceutico, Administrador, EncargadoInventario

admin.site.register(Empleado)
admin.site.register(Farmaceutico)
admin.site.register(Administrador)
admin.site.register(EncargadoInventario)
