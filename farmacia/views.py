from django.shortcuts import render, redirect

# Decorador personalizado para proteger vistas según tu sesión
def login_required_custom(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('usuario_id'):
            return redirect('login')  # redirige al login si no hay sesión
        return view_func(request, *args, **kwargs)
    return wrapper


# ---------------- VISTAS ----------------

@login_required_custom
def dashboard(request):
    usuario_nombre = request.session.get('usuario_nombre', 'Invitado')
    return render(request, "inicio.html", {"usuario_nombre": usuario_nombre})


@login_required_custom
def farmacia_view(request):
    return render(request, "farmacia.html")


@login_required_custom
def usuario_view(request):
    return render(request, "usuario.html")


@login_required_custom
def sucursal_view(request):
    return render(request, "sucursal.html")


@login_required_custom
def empleado_view(request):
    return render(request, "empleado.html")


@login_required_custom
def proveedor_view(request):
    return render(request, "proveedor.html")


@login_required_custom
def reporte_view(request):
    return render(request, "reporte.html")


@login_required_custom
def cliente_view(request):
    return render(request, "clientes/cliente.html")


@login_required_custom
def venta_view(request):
    return render(request, "venta.html")


@login_required_custom
def receta_view(request):
    return render(request, "receta.html")


@login_required_custom
def producto_view(request):
    return render(request, "producto.html")


@login_required_custom
def alerta_view(request):
    return render(request, "alerta.html")


@login_required_custom
def inventario_view(request):
    return render(request, "inventario.html")


@login_required_custom
def almacen_view(request):
    return render(request, "almacen.html")
