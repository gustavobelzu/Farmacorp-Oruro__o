# empleados/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm
from django.contrib import messages
from django.http import JsonResponse
from .models import Farmaceutico



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

            if nuevo_ci != empleado.ci:
                # Verificar que no exista otro empleado con el mismo CI
                if Empleado.objects.filter(ci=nuevo_ci).exclude(pk=empleado.pk).exists():
                    messages.error(request, f'El CI "{nuevo_ci}" ya existe.')
                else:
                    # Actualizamos manualmente todos los campos, incluyendo la PK
                    empleado.ci = nuevo_ci
                    empleado.nombre = form.cleaned_data['nombre']
                    empleado.telefono = form.cleaned_data['telefono']
                    empleado.salario = form.cleaned_data['salario']
                    empleado.cargo = form.cleaned_data['cargo']
                    empleado.sexo = form.cleaned_data['sexo']
                    empleado.estado = form.cleaned_data['estado']
                    empleado.turno = form.cleaned_data['turno']
                    empleado.fecha_ingreso = form.cleaned_data['fecha_ingreso']
                    empleado.fecha_salida = form.cleaned_data['fecha_salida']
                    empleado.id_farmacia = form.cleaned_data['id_farmacia']
                    empleado.save()
                    empleado_modificado = True
            else:
                # CI no cambió, actualizar normalmente
                form.save()
                empleado_modificado = True
    else:
        form = EmpleadoForm(instance=empleado)

    return render(request, 'empleados/editar_empleado.html', {
        'form': form,
        'empleado_modificado': empleado_modificado
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