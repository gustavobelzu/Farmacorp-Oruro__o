from django.shortcuts import render

def dashboard(request):
    usuario = request.user  # Django maneja el usuario autenticado
    return render(request, "inicio.html", {"usuario": usuario})
