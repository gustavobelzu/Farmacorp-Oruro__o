# farmacia/views_sucursal.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Sucursal
from .forms_sucursal import SucursalForm
from django.http import JsonResponse


# 🔹 Listar sucursales
def listar_sucursal(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'farmacia/listar_sucursal.html', {'sucursales': sucursales})

# 🔹 Crear sucursal
def crear_sucursal(request):
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Sucursal registrada correctamente.')
            return redirect('listar_sucursal')
    else:
        form = SucursalForm()
    return render(request, 'farmacia/crear_sucursal.html', {'form': form, 'accion': 'Registrar'})

# 🔹 Editar sucursal
def editar_sucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id=id)
    if request.method == 'POST':
        form = SucursalForm(request.POST, instance=sucursal)
        if form.is_valid():
            form.save()
            messages.success(request, '✏️ Sucursal actualizada correctamente.')
            return redirect('listar_sucursal')
    else:
        form = SucursalForm(instance=sucursal)
    return render(request, 'farmacia/editar_sucursal.html', {'form': form, 'accion': 'Editar'})

# 🔹 Eliminar sucursal
def eliminar_sucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id=id)
    sucursal.delete()
    messages.success(request, '🗑️ Sucursal eliminada correctamente.')
    return redirect('listar_sucursal')

# 🔹 Verificar si un NIT ya existe
def verificar_nit(request, nit):
    existe = Sucursal.objects.filter(nit=nit).exists()
    return JsonResponse({'existe': existe})