from django.shortcuts import render
from usuarios.models import Usuario

def dashboard(request):
    usuario = None
    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id=request.session['usuario_id'])
        except Usuario.DoesNotExist:
            pass
    return render(request, "inicio.html", {"usuario": usuario})
