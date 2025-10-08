from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib import messages

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/producto.html', {'productos': productos})

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProductoForm

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_listar')  # redirige al listado
    else:
        form = ProductoForm()
    return render(request, 'productos/crear_producto.html', {'form': form})

from django.contrib import messages

def editar_producto(request, codigo_barra):
    producto = get_object_or_404(Producto, codigo_barra=codigo_barra)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado correctamente')
            return redirect('producto_listar')  # redirige a la lista
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/editar_producto.html', {'form': form})


def eliminar_producto(request, codigo_barra):
    producto = get_object_or_404(Producto, codigo_barra=codigo_barra)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_listar')
    return redirect('producto_listar')
