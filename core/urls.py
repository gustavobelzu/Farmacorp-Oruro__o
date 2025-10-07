from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login')),  # Redirige "/" a "/login/"
    path('login/', include('usuarios.urls')),
    path('farmacia/', include('farmacia.urls')),
]
