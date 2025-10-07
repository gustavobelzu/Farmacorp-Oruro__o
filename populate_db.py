# populate_db.py
import os
import django

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

import random
from datetime import date, timedelta
from django.utils import timezone

from empleados.models import Empleado, Farmaceutico, Administrador, EncargadoInventario
from farmacia.models import Farmacia, Sucursal
from clientes.models import Cliente
from inventarios.models import Inventario, Almacen
from alertas.models import Alerta
from productos.models import Producto
from proveedores.models import Proveedor
from ventas.models import Venta, DetalleVenta
from recetas.models import Receta, DetalleReceta

# ---- BORRAR DATOS EXISTENTES ----
DetalleReceta.objects.all().delete()
Receta.objects.all().delete()
DetalleVenta.objects.all().delete()
Venta.objects.all().delete()
Cliente.objects.all().delete()
Proveedor.objects.all().delete()
Alerta.objects.all().delete()
Producto.objects.all().delete()
Inventario.objects.all().delete()
Farmaceutico.objects.all().delete()
Administrador.objects.all().delete()
EncargadoInventario.objects.all().delete()
Empleado.objects.all().delete()
almacen.objects.all().delete()

# ---------- UTILIDADES ----------
def random_date(start_year=2020, end_year=2025):
    start = date(start_year, 1, 1)
    end = date(end_year, 12, 31)
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

def random_choice(choices):
    return random.choice(choices)

# ---------- SUCURSAL Y FARMACIA ----------
sucursales = []
for i in range(1, 6):
    suc = Sucursal.objects.create(
        nombre=f"Sucursal {i}",
        departamento=f"Departamento {i}",
        nit=f"NIT{i:05}",
        email=f"sucursal{i}@mail.com",
        direccion=f"Calle {i} # {i*10}",
        horario="8:00-18:00",
        fecha_registro=random_date()
    )
    sucursales.append(suc)

farmacias = []
for i in range(1, 6):
    farm = Farmacia.objects.create(
        nombre_farmacia=f"Farmacia {i}",
        razon_legal=f"Razón {i}",
        id_sucursal=random_choice(sucursales)
    )
    farmacias.append(farm)

# ---------- EMPLEADOS Y SUBTIPOS ----------
empleados = []
for i in range(1, 21):
    emp = Empleado.objects.create(
        ci=f"18062{i:04}",
        nombre=f"Empleado {i}",
        telefono=f"70000{i:03}",
        salario=random.randint(1500, 3000),
        cargo=random_choice(["Encargado", "Farmaceutico", "Administrador"]),
        sexo=random_choice(["M", "F"]),
        estado="Activo",
        turno=random_choice(["Diurno", "Nocturno"]),
        fecha_ingreso=random_date(),
        fecha_salida=None,
        id_farmacia=random_choice(farmacias)
    )
    empleados.append(emp)

# Asignar roles
farmaceuticos = []
administradores = []
encargados = []
for emp in empleados:
    if emp.cargo == "Farmaceutico":
        f = Farmaceutico.objects.create(
            empleado=emp,
            matricula=f"M-{emp.ci}",
            especialidad=random_choice(["General", "Pediatria", "Cardiologia"])
        )
        farmaceuticos.append(f)
    elif emp.cargo == "Administrador":
        a = Administrador.objects.create(empleado=emp)
        administradores.append(a)
    elif emp.cargo == "Encargado":
        e = EncargadoInventario.objects.create(empleado=emp)
        encargados.append(e)

# ---------- CLIENTES ----------
clientes = []
for i in range(1, 21):
    cli = Cliente.objects.create(
        ci_cliente=f"10000{i:03}",
        nombre=f"Cliente {i}",
        telefono=f"60000{i:03}",
        direccion=f"Calle Cliente {i}",
        ci_empleado=random_choice(empleados)
    )
    clientes.append(cli)

# ---------- INVENTARIOS Y ALMACEN----------
# Crear almacenes
almacenes = []
for i in range(5):
    alm = Almacen.objects.create(
        categoria=random_choice(categorias),
        ubicacion=f"Bodega {i+1}",
        fecha_ingreso=random_date()
    )
    almacenes.append(alm)

# Crear inventarios asociados a un almacén
inventarios = []
for i in range(20):
    inv = Inventario.objects.create(
        cantidad=random.randint(10, 100),
        estado="Disponible",
        fecha_actualizacion=random_date(),
        stock_minimo=10,
        ci_encargado=random_choice(encargados),
        almacen=random_choice(almacenes)
    )
    inventarios.append(inv)
# ---------- ALERTAS ----------
alertas = []
for i in range(1, 21):
    a = Alerta.objects.create(
        tipo=random_choice(["Vencimiento", "Bajo stock", "Error de registro"]),
        descripcion=f"Descripcion alerta {i}",
        fecha_alerta=random_date(),
        estado="Pendiente",
        inventario=random_choice(inventarios)
    )
    alertas.append(a)

# ---------- PROVEEDORES ----------
proveedores = []
for i in range(1, 21):
    p = Proveedor.objects.create(
        nombre=f"Proveedor {i}",
        telefono=f"71000{i:03}",
        email=f"prov{i}@mail.com",
        direccion=f"Calle Proveedor {i}",
        estado="Activo",
        fecha_registro=random_date(),
        inventario=random_choice(inventarios)
    )
    proveedores.append(p)

# ---------- PRODUCTOS ----------
productos = []
for i in range(1, 21):
    prod = Producto.objects.create(
        codigo_barra=f"CB{i:05}",
        nombre=f"Producto {i}",
        descripcion=f"Descripcion producto {i}",
        estado="Disponible",
        precio_unitario=random.randint(10, 500),
        stock=random.randint(10, 100),
        fecha_vencimiento=random_date(),
        iva="13%",
        id_inventario=random_choice(inventarios),
        ci_cliente=random_choice(clientes)
    )
    productos.append(prod)

# ---------- VENTAS Y DETALLES ----------
ventas = []
for i in range(1, 21):
    v = Venta.objects.create(
        factura=random_choice([True, False]),
        fecha=random_date(),
        total=random.randint(100, 1000),
        estado="Pagado",
        cliente=random_choice(clientes)
    )
    ventas.append(v)

for v in ventas:
    for j in range(2):  # 2 detalles por venta
        DetalleVenta.objects.create(
            cantidad=random.randint(1, 5),
            precio_unitario=random.randint(10, 200),
            subtotal=random.randint(10, 500),
            metodo_pago=random_choice(["Efectivo", "Tarjeta"]),
            descuento=random_choice([True, False]),
            venta=v
        )

# ---------- RECETAS Y DETALLES ----------
recetas = []
for i in range(1, 21):
    r = Receta.objects.create(
        id_receta=f"R{i:04}",
        fecha_emision=random_date(),
        matricula_medico=random_choice(farmaceuticos).matricula if farmaceuticos else "M-0000",
        medicamento=random_choice(productos).nombre if productos else "Medicamento X",
        cantidad=random.randint(1, 10),
        cliente=random_choice(clientes)
    )
    recetas.append(r)

for r in recetas:
    for j in range(2):
        DetalleReceta.objects.create(
            dosis="1 pastilla",
            frecuencia="2 veces al día",
            duracion="5 días",
            instrucciones="Tomar después de comer",
            receta=r
        )

print("¡Datos de prueba insertados correctamente!")
