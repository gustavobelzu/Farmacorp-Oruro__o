from django.shortcuts import render

# Create your views here.
def inicio(request):
    if 'user_id' not in request.session:
        return redirect('login')  # Si no hay sesión, redirige al login
    return render(request, 'farmacia/inicio.html')


def inicio(request):
    return render(request, 'login.html')  # Cambia 'login.html' por 'inicio.html' si lo deseas


