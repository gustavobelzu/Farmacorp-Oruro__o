from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

def listar_productos(request):
    productos = Producto.objects.all()  # Trae todos los productos
    return render(request, 'producto.html', {'productos': productos})

# Crear producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_listar')  # Asegúrate que el nombre coincida
    else:
        form = ProductoForm()
    return render(request, 'crear.html', {'form': form})


# Editar producto
def editar_producto(request, codigo_barra):
    producto = get_object_or_404(Producto, codigo_barra=codigo_barra)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto.html', {'form': form, 'producto': producto})

# Eliminar producto
def eliminar_producto(request, codigo_barra):
    producto = get_object_or_404(Producto, codigo_barra=codigo_barra)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'producto.html', {'producto': producto})
