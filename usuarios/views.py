from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario
from django.utils import timezone
from datetime import timedelta

MAX_INTENTOS = 3
TIEMPO_BLOQUEO = 10  # segundos

def login_view(request):
    if 'intentos' not in request.session:
        request.session['intentos'] = 0
    if 'bloqueo_hasta' not in request.session:
        request.session['bloqueo_hasta'] = None

    ahora = timezone.now()
    bloqueo_hasta = request.session.get('bloqueo_hasta')
    tiempo_restante = 0
    intentos_restantes = MAX_INTENTOS - request.session['intentos']

    # Bloqueo activo
    if bloqueo_hasta:
        bloqueo_hasta = timezone.datetime.fromisoformat(bloqueo_hasta)
        if ahora < bloqueo_hasta:
            tiempo_restante = int((bloqueo_hasta - ahora).total_seconds())
            return render(request, "usuarios/login.html", {
                'bloqueo': True,
                'tiempo_restante': tiempo_restante
            })
        else:
            # desbloquear
            request.session['bloqueo_hasta'] = None
            request.session['intentos'] = 0
            intentos_restantes = MAX_INTENTOS

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            usuario = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            request.session['intentos'] += 1
            intentos_restantes = MAX_INTENTOS - request.session['intentos']
            if request.session['intentos'] >= MAX_INTENTOS:
                request.session['bloqueo_hasta'] = (ahora + timedelta(seconds=TIEMPO_BLOQUEO)).isoformat()
                request.session['intentos'] = 0
                return render(request, "usuarios/login.html", {
                    'bloqueo': True,
                    'tiempo_restante': TIEMPO_BLOQUEO
                })
            return render(request, "usuarios/login.html", {'intentos_restantes': intentos_restantes})

        if usuario.check_password(password):
            request.session['usuario_id'] = usuario.id
            request.session['usuario_nombre'] = usuario.username
            request.session['intentos'] = 0
            request.session['bloqueo_hasta'] = None
            return redirect('dashboard')
        else:
            request.session['intentos'] += 1
            intentos_restantes = MAX_INTENTOS - request.session['intentos']
            if request.session['intentos'] >= MAX_INTENTOS:
                request.session['bloqueo_hasta'] = (ahora + timedelta(seconds=TIEMPO_BLOQUEO)).isoformat()
                request.session['intentos'] = 0
                return render(request, "usuarios/login.html", {
                    'bloqueo': True,
                    'tiempo_restante': TIEMPO_BLOQUEO
                })
            return render(request, "usuarios/login.html", {'intentos_restantes': intentos_restantes})

    return render(request, "usuarios/login.html", {'intentos_restantes': intentos_restantes})


def logout_view(request):
    """Cerrar sesión y volver al login"""
    request.session.flush()  # elimina toda la sesión del usuario
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('login')
