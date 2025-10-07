# usuarios/views.py
from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages
from django.contrib.auth.hashers import check_password

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = Usuario.objects.get(username=username)
            if check_password(password, user.password):
                # Guardar info de sesión
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                return redirect('inicio')  # Redirige a la página principal después del login
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
        except Usuario.DoesNotExist:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "inicio.html")
