from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'login.html')  # Cambia 'login.html' por 'inicio.html' si lo deseas
