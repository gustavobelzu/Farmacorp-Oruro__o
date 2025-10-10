from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from .models import Usuario
from django.contrib import messages



MAX_INTENTOS = 3
TIEMPO_BLOQUEO = 5  # segundos de bloqueo

def login_view(request):
    # Inicializar sesión
    if 'intentos' not in request.session:
        request.session['intentos'] = 0
    if 'bloqueo_hasta' not in request.session:
        request.session['bloqueo_hasta'] = None

    ahora = timezone.now()
    bloqueo_hasta = request.session.get('bloqueo_hasta')
    intentos_restantes = MAX_INTENTOS - request.session['intentos']

    # Verificar bloqueo
    if bloqueo_hasta:
        bloqueo_hasta = timezone.datetime.fromisoformat(bloqueo_hasta)
        if ahora < bloqueo_hasta:
            tiempo_restante = int((bloqueo_hasta - ahora).total_seconds())
            return render(request, "usuarios/login.html", {
                'bloqueo': True,
                'tiempo_restante': tiempo_restante,
            })
        else:
            request.session['bloqueo_hasta'] = None
            request.session['intentos'] = 0
            intentos_restantes = MAX_INTENTOS

    form_data = {'username': ''}
    usuario_no_encontrado = False
    password_incorrecta = False

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        form_data['username'] = username

        try:
            usuario = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            request.session['intentos'] += 1
            intentos_restantes = MAX_INTENTOS - request.session['intentos']
            usuario_no_encontrado = True
            if request.session['intentos'] >= MAX_INTENTOS:
                request.session['bloqueo_hasta'] = (ahora + timedelta(seconds=TIEMPO_BLOQUEO)).isoformat()
                request.session['intentos'] = 0
                return render(request, "usuarios/login.html", {
                    'bloqueo': True,
                    'tiempo_restante': TIEMPO_BLOQUEO,
                    'form_data': form_data
                })
            return render(request, "usuarios/login.html", {
                'intentos_restantes': intentos_restantes,
                'form_data': form_data,
                'usuario_no_encontrado': usuario_no_encontrado,
                'password_incorrecta': password_incorrecta
            })

        if not usuario.check_password(password):
            request.session['intentos'] += 1
            intentos_restantes = MAX_INTENTOS - request.session['intentos']
            password_incorrecta = True
            if request.session['intentos'] >= MAX_INTENTOS:
                request.session['bloqueo_hasta'] = (ahora + timedelta(seconds=TIEMPO_BLOQUEO)).isoformat()
                request.session['intentos'] = 0
                return render(request, "usuarios/login.html", {
                    'bloqueo': True,
                    'tiempo_restante': TIEMPO_BLOQUEO,
                    'form_data': form_data
                })
            return render(request, "usuarios/login.html", {
                'intentos_restantes': intentos_restantes,
                'form_data': form_data,
                'usuario_no_encontrado': usuario_no_encontrado,
                'password_incorrecta': password_incorrecta
            })

        # Login exitoso
        request.session['usuario_id'] = usuario.id
        request.session['usuario_nombre'] = usuario.username
        request.session['intentos'] = 0
        request.session['bloqueo_hasta'] = None
        return redirect('dashboard')

    return render(request, "usuarios/login.html", {
        'intentos_restantes': intentos_restantes,
        'form_data': form_data,
        'usuario_no_encontrado': usuario_no_encontrado,
        'password_incorrecta': password_incorrecta
    })



def logout_view(request):
    """Cerrar sesión y volver al login"""
    request.session.flush()
    #messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('login')
