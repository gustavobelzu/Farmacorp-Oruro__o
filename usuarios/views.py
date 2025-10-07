# usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            usuario = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            messages.error(request, "❌ El usuario no existe.")
            return render(request, "usuarios/login.html")

        # Verifica contraseña con tu método personalizado
        if usuario.check_password(password):
            # Guardar datos de sesión
            request.session['usuario_id'] = usuario.id_usuario
            request.session['usuario_nombre'] = usuario.username

            messages.success(request, f"✅ Bienvenido {usuario.username}")
            return redirect('farmacia_dashboard')  # nombre exacto de tu ruta en farmacia/urls.py
        else:
            messages.error(request, "⚠️ Contraseña incorrecta.")
            return render(request, "usuarios/login.html")

    return render(request, "usuarios/login.html")


def logout_view(request):
    """Cerrar sesión y volver al login"""
    request.session.flush()  # elimina toda la sesión del usuario
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('login')
