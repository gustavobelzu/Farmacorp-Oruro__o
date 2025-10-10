from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib import messages

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/producto.html', {'productos': productos})

from django.shortcuts import render, redirect
from .forms import ProductoForm

def crear_producto(request):
    form = ProductoForm(request.POST or None)
    producto_guardado = False  # ← indicador de éxito

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            producto_guardado = True  # ← marcar como guardado

    return render(request, 'productos/crear_producto.html', {
        'form': form,
        'producto_guardado': producto_guardado  # ← se envía al template
    })

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
    producto_eliminado = False
    producto = get_object_or_404(Producto, codigo_barra=codigo_barra)

    if request.method == 'POST':
        producto.delete()
        producto_eliminado = True  # ← marcamos que se eliminó correctamente

    productos = Producto.objects.all()
    return render(request, 'productos/producto.html', {
        'productos': productos,
        'producto_eliminado': producto_eliminado
    })