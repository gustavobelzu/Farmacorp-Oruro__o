import os
import django
import random
from datetime import datetime, timedelta
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tu_proyecto.settings')  # reemplaza 'tu_proyecto'
django.setup()

from empleados.models import Empleado, Farmaceutico, Administrador, EncargadoInventario
from clientes.models import Cliente
from farmacia.models import Farmacia
from productos.models import Producto
from inventarios.models import Inventario, Alerta
from proveedores.models import Proveedor
from ventas.models import Venta, DetalleVenta
from recetas.models import Receta, DetalleReceta
from reportes.models import Reporte
from account.models import Usuario



fake = Faker()

# ================================
# Empleados
# ================================
empleados = []
for _ in range(20):
    emp = Empleado.objects.create(
        ci=fake.unique.ssn(),
        nombre=fake.name(),
        telefono=fake.phone_number(),
        salario=random.randint(3000, 10000),
        cargo=random.choice(['Farmaceutico', 'Administrador', 'EncargadoInventario']),
        sexo=random.choice(['M', 'F']),
        estado=random.choice(['Activo', 'Inactivo']),
        turno=random.choice(['Mañana', 'Tarde']),
        fechaIngreso=fake.date_between(start_date='-5y', end_date='today'),
        fechaSalida=None
    )
    empleados.append(emp)

# ================================
# Farmacias
# ================================
farmacias = []
for _ in range(5):
    f = Farmacia.objects.create(
        nombre_farmacia=fake.company(),
        razonLegal=fake.company_suffix(),
        id_sucursal=None
    )
    farmacias.append(f)

# ================================
# Clientes
# ================================
clientes = []
for _ in range(20):
    c = Cliente.objects.create(
        ci_cliente=fake.unique.ssn(),
        nombre=fake.name(),
        telefono=fake.phone_number(),
        direccion=fake.address()
    )
    clientes.append(c)

# ================================
# Inventarios y Productos
# ================================
inventarios = []
for _ in range(20):
    inv = Inventario.objects.create(
        cantidad=random.randint(10, 100),
        estado=random.choice(['Bueno', 'Malo']),
        fecha_actualizacion=fake.date_this_year(),
        stock_minimo=random.randint(5, 20),
        ci_encargado=random.choice(empleados)
    )
    inventarios.append(inv)

productos = []
for _ in range(20):
    p = Producto.objects.create(
        codigoBarra=fake.unique.ean13(),
        nombre=fake.word(),
        descripcion=fake.text(max_nb_chars=50),
        estado=random.choice(['Disponible', 'Agotado']),
        precioUnitario=random.uniform(5, 200),
        stock=random.randint(0, 100),
        fechaVencimiento=fake.date_between(start_date='today', end_date='+2y'),
        iva=random.choice(['5%', '10%']),
        id_inventario=random.choice(inventarios)
    )
    productos.append(p)

# ================================
# Proveedores
# ================================
proveedores = []
for _ in range(20):
    pr = Proveedor.objects.create(
        nombre=fake.company(),
        telefono=fake.phone_number(),
        email=fake.email(),
        direccion=fake.address(),
        estado='Activo',
        fecha_registro=fake.date_this_decade(),
        id_inventario=random.choice(inventarios)
    )
    proveedores.append(pr)

# ================================
# Ventas y Detalles
# ================================
ventas = []
for _ in range(20):
    v = Venta.objects.create(
        factura=True,
        fecha=fake.date_this_year(),
        total=random.uniform(50, 500),
        estado='Completada',
        ci_cliente=random.choice(clientes)
    )
    ventas.append(v)

for v in ventas:
    for _ in range(2):  # 2 detalles por venta
        DetalleVenta.objects.create(
            cantidad=random.randint(1, 5),
            precioUnitario=random.uniform(5, 200),
            subtotal=random.uniform(5, 500),
            metodoPago=random.choice(['Efectivo', 'Tarjeta']),
            descuento=random.choice([True, False]),
            id_venta=v
        )

# ================================
# Recetas y Detalles
# ================================
recetas = []
for _ in range(20):
    r = Receta.objects.create(
        id_receta=fake.unique.uuid4(),
        fecha_emision=fake.date_this_year(),
        matricula_medico=fake.bothify(text='MED####'),
        medicamento=fake.word(),
        cantidad=random.randint(1, 5),
        ci_cliente=random.choice(clientes)
    )
    recetas.append(r)

for r in recetas:
    DetalleReceta.objects.create(
        dosis=f"{random.randint(1, 2)} pastillas",
        frecuencia=random.choice(['Diaria', 'Cada 8 horas']),
        duracion=f"{random.randint(3, 10)} días",
        instrucciones=fake.sentence(),
        id_receta=r
    )

# ================================
# Reportes
# ================================
for _ in range(20):
    Reporte.objects.create(
        fecha_reporte=fake.date_this_year(),
        tipo=random.choice(['Inventario', 'Venta']),
        ci_empleado=random.choice(empleados)
    )

# ================================
# Usuarios
# ================================
for _ in range(5):
    Usuario.objects.create(
        username=fake.user_name(),
        password='password123',  # no encriptado para pruebas
        fecha_creacion=datetime.today(),
        ci_empleado=random.choice(empleados)
    )

print("¡Datos insertados correctamente!")
