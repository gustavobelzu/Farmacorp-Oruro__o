from django.shortcuts import render, redirect
from django.contrib import messages
from usuarios.models import Usuario

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            usuario = Usuario.objects.get(username=username)
            if usuario.check_password(password):
                request.session['user_id'] = usuario.id_usuario  # Guardar usuario en sesión
                return redirect('inicio')
            else:
                messages.error(request, "Contraseña incorrecta.")
        except Usuario.DoesNotExist:
            messages.error(request, "Usuario no encontrado.")

    return render(request, "login.html")


def logout_view(request):
    try:
        del request.session['user_id']  # Eliminar usuario de la sesión
    except KeyError:
        pass
    return redirect('login')
