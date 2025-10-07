from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Usuario.objects.get(username=username)
            if user.check_password(password):
                # Guardar usuario en sesión
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                messages.success(request, f"Bienvenido, {user.username}!")
                return redirect('farmacia_inicio')  # Cambia 'farmacia_inicio' al name de tu view principal
            else:
                messages.error(request, "Contraseña incorrecta.")
        except Usuario.DoesNotExist:
            messages.error(request, "Usuario no encontrado.")

    return render(request, 'login.html')
