from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
from django.contrib import messages

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente registrado correctamente.")
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/registrar_cliente.html', {'form': form})

def editar_cliente(request, ci_cliente):
    cliente = get_object_or_404(Cliente, pk=ci_cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente actualizado correctamente.")
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/editar_cliente.html', {'form': form, 'cliente': cliente})

def eliminar_cliente(request, ci_cliente):
    cliente = get_object_or_404(Cliente, pk=ci_cliente)
    cliente.delete()
    messages.warning(request, "Cliente eliminado correctamente.")
    return redirect('listar_clientes')
