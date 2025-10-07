# farmacia/views.py
from django.shortcuts import render, redirect
from usuarios.models import Usuario

def inicio(request):
    # Obtener usuario de sesión si existe
    usuario_id = request.session.get('user_id')
    usuario = None
    if usuario_id:
        try:
            usuario = Usuario.objects.get(id_usuario=usuario_id)
        except Usuario.DoesNotExist:
            pass

    return render(request, 'inicio.html', {'usuario': usuario})
