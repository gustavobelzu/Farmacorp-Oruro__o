# farmacia/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Farmacia, Sucursal
from .forms import FarmaciaForm

# ---------------- VISTAS ----------------
# Decorador personalizado para proteger vistas
def login_required_custom(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('usuario_id'):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper
# ------------------------------------------

# -------------------- DASHBOARD --------------------
@login_required_custom
def dashboard(request):
    usuario_nombre = request.session.get('usuario_nombre', 'Invitado')
    return render(request, "inicio.html", {"usuario_nombre": usuario_nombre})

# -------------------- VISTAS GENERALES --------------------
@login_required_custom
def farmacia_view(request):
    return render(request, "farmacia/farmacia.html")

@login_required_custom
def usuario_view(request):
    return render(request, "usuario.html")

@login_required_custom
def sucursal_view(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'farmacia/listar_sucursal.html', {'sucursales': sucursales})

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

# -------------------- CRUD FARMACIA --------------------

# Listar farmacias de una sucursal
@login_required_custom
def listar_farmacia(request):
    farmacias = Farmacia.objects.all()
    return render(request, 'farmacia/listar_farmacia.html', {
        'farmacias': farmacias
    })

@login_required_custom
def crear_farmacia(request):
    farmacia_guardada = False
    if request.method == 'POST':
        form = FarmaciaForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a la lista de farmacias después de guardar
            messages.success(request, '✅ Farmacia guardada correctamente.')
            return redirect('farmacia:listar_farmacia')
    else:
        form = FarmaciaForm()
    
    return render(request, 'farmacia/crear_farmacia.html', {
        'form': form,
        'farmacia_guardada': farmacia_guardada
    })

# Editar farmacia
@login_required_custom
def editar_farmacia(request, id):
    farmacia = get_object_or_404(Farmacia, id=id)
    if request.method == 'POST':
        form = FarmaciaForm(request.POST, instance=farmacia)
        if form.is_valid():
            form.save()
            messages.success(request, '✏️ Farmacia actualizada correctamente.')
            return redirect('farmacia:listar_farmacia')
    else:
        form = FarmaciaForm(instance=farmacia)
    return render(request, 'farmacia/editar_farmacia.html', {'form': form, 'accion': 'Editar'})

# Eliminar farmacia
@login_required_custom
def eliminar_farmacia(request, id):
    farmacia = get_object_or_404(Farmacia, id=id)
    farmacia.delete()
    messages.success(request, '🗑️ Farmacia eliminada correctamente.')
    return redirect('farmacia:listar_farmacia')

# -------------------- AJAX: Verificar farmacia por nombre --------------------
# 🔹 Verificar si el nombre de la farmacia ya existe (AJAX)
@login_required_custom
def verificar_farmacia(request, nombre):
    nombre = nombre.strip()
    existe = Farmacia.objects.filter(nombre_farmacia__iexact=nombre).exists()
    return JsonResponse({'existe': existe})

