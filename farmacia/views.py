from django.shortcuts import render
from usuarios.models import Usuario

def inicio(request):
    usuario = None
    user_id = request.session.get('user_id')
    if user_id:
        try:
            usuario = Usuario.objects.get(id_usuario=user_id)
        except Usuario.DoesNotExist:
            pass

    return render(request, "inicio.html", {"usuario": usuario})
