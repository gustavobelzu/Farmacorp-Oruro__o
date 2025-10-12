# empleados/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm
from django.contrib import messages
from django.http import JsonResponse
from .models import Empleado, Farmaceutico, Administrador, EncargadoInventario




# ======================
# Listar Empleados
# ======================
def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/empleado.html', {'empleados': empleados})

# ======================
# Crear Empleado
# ======================
def crear_empleado(request):
    form = EmpleadoForm(request.POST or None)
    empleado_guardado = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            empleado_guardado = True

    return render(request, 'empleados/crear_empleado.html', {
        'form': form,
        'empleado_guardado': empleado_guardado
    })

# ======================
# Editar Empleado
# ======================
def editar_empleado(request, ci):
    empleado = get_object_or_404(Empleado, ci=ci)
    empleado_modificado = False

    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            nuevo_ci = form.cleaned_data['ci']

            # --- Verificar duplicado de CI si cambió ---
            if nuevo_ci != empleado.ci and Empleado.objects.filter(ci=nuevo_ci).exclude(pk=empleado.pk).exists():
                messages.error(request, f'El CI "{nuevo_ci}" ya existe.')
            else:
                # Guardamos los datos principales del empleado
                empleado = form.save(commit=False)
                empleado.ci = nuevo_ci
                empleado.save()

                # === Manejo del tipo de empleado ===
                tipo = request.POST.get('tipo_empleado', '').lower()

                # Limpiar roles previos (solo puede tener uno)
                Farmaceutico.objects.filter(empleado=empleado).delete()
                Administrador.objects.filter(empleado=empleado).delete()
                EncargadoInventario.objects.filter(empleado=empleado).delete()

                # Crear según el tipo seleccionado
                if tipo == 'farmaceutico':
                    Farmaceutico.objects.create(
                        empleado=empleado,
                        matricula=request.POST.get('matricula'),
                        especialidad=request.POST.get('especialidad')
                    )
                elif tipo == 'administrador':
                    Administrador.objects.create(empleado=empleado)
                elif tipo == 'encargado inventario':
                    EncargadoInventario.objects.create(empleado=empleado)
                # Si eliges otro tipo, no se crea ningún modelo adicional

                empleado_modificado = True

    else:
        form = EmpleadoForm(instance=empleado)

    return render(request, 'empleados/editar_empleado.html', {
        'form': form,
        'empleado_modificado': empleado_modificado,
        'empleado': empleado,
    })


# ======================
# Eliminar Empleado
# ======================
def eliminar_empleado(request, ci):
    empleado_eliminado = False
    empleado = get_object_or_404(Empleado, ci=ci)

    if request.method == 'POST':
        empleado.delete()
        empleado_eliminado = True

    empleados = Empleado.objects.all()
    return render(request, 'empleados/empleado.html', {
        'empleados': empleados,
        'empleado_eliminado': empleado_eliminado
    })

# ======================
# Verificar existencia
# ======================
def verificar_empleado(request, ci):
    existe = Empleado.objects.filter(ci=ci).exists()
    return JsonResponse({'existe': existe})

def verificar_matricula(request, matricula):
    existe = Farmaceutico.objects.filter(matricula=matricula).exists()
    return JsonResponse({'existe': existe})