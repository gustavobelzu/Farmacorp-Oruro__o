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
                request.session['usuario_id'] = usuario.id
                return redirect('dashboard')  # nombre del view en farmacia/urls.py
            else:
                messages.error(request, "Contraseña incorrecta")
        except Usuario.DoesNotExist:
            messages.error(request, "Usuario no existe")
    return render(request, "login.html")

def logout_view(request):
    request.session.flush()  # Limpiar sesión
    return redirect('login')
