from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib import messages
from django.http import JsonResponse

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/producto.html', {'productos': productos})

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
    # Obtenemos el producto existente
    producto = get_object_or_404(Producto, codigo_barra=codigo_barra)
    producto_modificado = False

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            nuevo_codigo = form.cleaned_data['codigo_barra']

            if nuevo_codigo != producto.codigo_barra:
                # Verificar que no exista otro producto con el mismo código
                if Producto.objects.filter(codigo_barra=nuevo_codigo).exclude(pk=producto.pk).exists():
                    messages.error(request, f'El código "{nuevo_codigo}" ya existe.')
                else:
                    # Actualizar manualmente todos los campos, incluyendo la PK
                    producto.codigo_barra = nuevo_codigo
                    producto.nombre = form.cleaned_data['nombre']
                    producto.descripcion = form.cleaned_data['descripcion']
                    producto.estado = form.cleaned_data['estado']
                    producto.precio_unitario = form.cleaned_data['precio_unitario']
                    producto.stock = form.cleaned_data['stock']
                    producto.fecha_vencimiento = form.cleaned_data['fecha_vencimiento']
                    producto.iva = form.cleaned_data['iva']
                    producto.id_inventario = form.cleaned_data['id_inventario']
                    producto.ci_cliente = form.cleaned_data['ci_cliente']
                    producto.save()
                    producto_modificado = True
            else:
                # Código no cambió, actualizar otros campos normalmente
                form.save()
                producto_modificado = True
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'productos/editar_producto.html', {
        'form': form,
        'producto_modificado': producto_modificado
    })


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

def verificar_producto(request, codigo):
    existe = Producto.objects.filter(codigo_barra=codigo).exists()
    return JsonResponse({'existe': existe})
