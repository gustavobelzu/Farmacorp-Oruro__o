# farmacia/view_sucursal.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Sucursal
from .forms_sucursal import SucursalForm
from django.contrib import messages
from django.http import JsonResponse

# ==========================
# Listar sucursales
# ==========================
def listar_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'farmacia/sucursal.html', {'sucursales': sucursales})

# ==========================
# Crear sucursal
# ==========================
def crear_sucursal(request):
    form = SucursalForm(request.POST or None)
    sucursal_guardada = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            sucursal_guardada = True

    return render(request, 'farmacia/crear_sucursal.html', {
        'form': form,
        'sucursal_guardada': sucursal_guardada
    })

# ==========================
# Editar sucursal
# ==========================
def editar_sucursal(request, pk):
    sucursal = get_object_or_404(Sucursal, pk=pk)
    sucursal_modificada = False

    if request.method == 'POST':
        form = SucursalForm(request.POST, instance=sucursal)
        if form.is_valid():
            # Aquí puedes verificar campos únicos si quieres
            form.save()
            sucursal_modificada = True
    else:
        form = SucursalForm(instance=sucursal)

    return render(request, 'farmacia/editar_sucursal.html', {
        'form': form,
        'sucursal_modificada': sucursal_modificada
    })

# ==========================
# Eliminar sucursal
# ==========================
def eliminar_sucursal(request, pk):
    sucursal_eliminada = False
    sucursal = get_object_or_404(Sucursal, pk=pk)

    if request.method == 'POST':
        sucursal.delete()
        sucursal_eliminada = True

    sucursales = Sucursal.objects.all()
    return render(request, 'farmacia/sucursal.html', {
        'sucursales': sucursales,
        'sucursal_eliminada': sucursal_eliminada
    })

# ==========================
# Verificar existencia de sucursal por NIT o nombre
# ==========================
def verificar_sucursal(request):
    nombre = request.GET.get('nombre', '')
    nit = request.GET.get('nit', '')

    existe = Sucursal.objects.filter(nombre=nombre).exists() or Sucursal.objects.filter(nit=nit).exists()
    return JsonResponse({'existe': existe})
