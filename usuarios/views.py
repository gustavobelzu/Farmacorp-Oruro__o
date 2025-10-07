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
            messages.error(request, "Usuario no existe")
            return render(request, "login.html")

        if usuario.check_password(password):
            # Guardar en sesión
            request.session['usuario_id'] = usuario.id_usuario
            return redirect('dashboard')  # redirige a farmacia/dashboard
        else:
            messages.error(request, "Contraseña incorrecta")
            return render(request, "login.html")

    return render(request, "login.html")


def logout_view(request):
    if 'usuario_id' in request.session:
        del request.session['usuario_id']
    return redirect('login')
