from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Farmacia

# farmacia/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Farmacia, Sucursal
from .forms import FarmaciaForm

# ======================
# Listar Farmacias
# ======================
def listar_farmacias(request):
    farmacias = Farmacia.objects.select_related('id_sucursal').all()
    return render(request, 'farmacia/farmacia.html', {'farmacias': farmacias})


# ======================
# Crear Farmacia
# ======================
def crear_farmacia(request):
    form = FarmaciaForm(request.POST or None)
    farmacia_guardada = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            farmacia_guardada = True
            messages.success(request, "Farmacia registrada correctamente.")
        else:
            messages.error(request, "Por favor, corrige los errores del formulario.")

    return render(request, 'farmacia/crear_farmacia.html', {
        'form': form,
        'farmacia_guardada': farmacia_guardada
    })


# ======================
# Editar Farmacia
# ======================
def editar_farmacia(request, pk):
    farmacia = get_object_or_404(Farmacia, pk=pk)
    farmacia_modificada = False

    if request.method == 'POST':
        form = FarmaciaForm(request.POST, instance=farmacia)
        if form.is_valid():
            form.save()
            farmacia_modificada = True
            messages.success(request, "Farmacia actualizada correctamente.")
        else:
            messages.error(request, "Por favor, corrige los errores del formulario.")
    else:
        form = FarmaciaForm(instance=farmacia)

    return render(request, 'farmacia/editar_farmacia.html', {
        'form': form,
        'farmacia_modificada': farmacia_modificada,
        'farmacia': farmacia
    })


# ======================
# Eliminar Farmacia
# ======================
def eliminar_farmacia(request, pk):
    farmacia = get_object_or_404(Farmacia, pk=pk)
    farmacia_eliminada = False

    if request.method == 'POST':
        farmacia.delete()
        farmacia_eliminada = True
        messages.success(request, "Farmacia eliminada correctamente.")

    farmacias = Farmacia.objects.select_related('id_sucursal').all()
    return render(request, 'farmacia/farmacia.html', {
        'farmacias': farmacias,
        'farmacia_eliminada': farmacia_eliminada
    })


# ======================
# Verificar existencia
# ======================
def verificar_farmacia(request, nombre):
    existe = Farmacia.objects.filter(nombre_farmacia=nombre).exists()
    return JsonResponse({'existe': existe})


# ---------------- VISTAS ----------------
# ======================
# Decorador personalizado para proteger vistas
# ======================
def login_required_custom(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('usuario_id'):
            return redirect('login')  # Redirige al login si no hay sesión activa
        return view_func(request, *args, **kwargs)
    return wrapper

@login_required_custom
def dashboard(request):
    usuario_nombre = request.session.get('usuario_nombre', 'Invitado')
    return render(request, "inicio.html", {"usuario_nombre": usuario_nombre})


@login_required_custom
def farmacia_view(request):
    return render(request, "farmacia.html")


@login_required_custom
def usuario_view(request):
    return render(request, "usuario.html")


@login_required_custom
def sucursal_view(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'farmacia/farmacia.html', {'sucursales': sucursales})


@login_required_custom
def empleado_view(request):
    return render(request, "empleado.html")


@login_required_custom
def proveedor_view(request):
    return render(request, "proveedor.html")


@login_required_custom
def reporte_view(request):
    return render(request, "reporte.html")


@login_required_custom
def cliente_view(request):
    return render(request, "cliente.html")


@login_required_custom
def venta_view(request):
    return render(request, "venta.html")


@login_required_custom
def receta_view(request):
    return render(request, "receta.html")


@login_required_custom
def producto_view(request):
    return render(request, "producto.html")


@login_required_custom
def alerta_view(request):
    return render(request, "alerta.html")


@login_required_custom
def inventario_view(request):
    return render(request, "inventario.html")


@login_required_custom
def almacen_view(request):
    return render(request, "almacen.html")
