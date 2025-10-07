from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    usuario = request.user
    return render(request, "inicio.html", {"usuario": usuario})

@login_required
def farmacia_view(request):
    return render(request, "farmacia.html")

@login_required
def usuario_view(request):
    return render(request, "usuario.html")

@login_required
def sucursal_view(request):
    return render(request, "sucursal.html")

@login_required
def empleado_view(request):
    return render(request, "empleado.html")

@login_required
def proveedor_view(request):
    return render(request, "proveedor.html")

@login_required
def reporte_view(request):
    return render(request, "reporte.html")

@login_required
def cliente_view(request):
    return render(request, "cliente.html")

@login_required
def venta_view(request):
    return render(request, "venta.html")

@login_required
def receta_view(request):
    return render(request, "receta.html")

@login_required
def producto_view(request):
    return render(request, "producto.html")

@login_required
def alerta_view(request):
    return render(request, "alerta.html")

@login_required
def inventario_view(request):
    return render(request, "inventario.html")

@login_required
def almacen_view(request):
    return render(request, "almacen.html")