from django.shortcuts import render
from usuarios.models import Usuario

def dashboard(request):
    usuario = None
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        try:
            usuario = Usuario.objects.get(id_usuario=usuario_id)
        except Usuario.DoesNotExist:
            pass

    return render(request, "inicio.html", {"usuario": usuario})
