from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Cliente
from .forms import ClienteForm

# ===== Listar clientes =====
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente.html', {'clientes': clientes})

# ===== Crear cliente =====
def crear_cliente(request):
    form = ClienteForm(request.POST or None)
    cliente_guardado = False

    if request.method == 'POST':
        if form.is_valid():
            ci = form.cleaned_data['ci_cliente']
            if Cliente.objects.filter(ci_cliente=ci).exists():
                messages.error(request, f'El cliente con CI "{ci}" ya existe.')
            else:
                form.save()
                cliente_guardado = True

    return render(request, 'clientes/crear_cliente.html', {
        'form': form,
        'cliente_guardado': cliente_guardado
    })

# ===== Editar cliente =====
def editar_cliente(request, ci_cliente):
    cliente = get_object_or_404(Cliente, ci_cliente=ci_cliente)
    cliente_modificado = False

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            nuevo_ci = form.cleaned_data['ci_cliente']

            if nuevo_ci != cliente.ci_cliente:
                if Cliente.objects.filter(ci_cliente=nuevo_ci).exclude(pk=cliente.pk).exists():
                    messages.error(request, f'El CI "{nuevo_ci}" ya existe.')
                else:
                    # Actualizar manualmente incluyendo la PK
                    cliente.ci_cliente = nuevo_ci
                    cliente.nombre = form.cleaned_data['nombre']
                    cliente.telefono = form.cleaned_data['telefono']
                    cliente.direccion = form.cleaned_data['direccion']
                    cliente.ci_empleado = form.cleaned_data['ci_empleado']
                    cliente.save()
                    cliente_modificado = True
            else:
                form.save()
                cliente_modificado = True
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'clientes/editar_cliente.html', {
        'form': form,
        'cliente_modificado': cliente_modificado
    })

# ===== Eliminar cliente =====
def eliminar_cliente(request, ci_cliente):
    cliente_eliminado = False
    cliente = get_object_or_404(Cliente, ci_cliente=ci_cliente)

    if request.method == 'POST':
        cliente.delete()
        cliente_eliminado = True

    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente.html', {
        'clientes': clientes,
        'cliente_eliminado': cliente_eliminado
    })

# ===== Verificar existencia de cliente =====
def verificar_cliente(request, ci):
    existe = Cliente.objects.filter(ci_cliente=ci).exists()
    return JsonResponse({'existe': existe})
