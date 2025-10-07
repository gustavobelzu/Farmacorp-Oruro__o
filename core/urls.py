from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login')),  # Redirige "/" a "/login/"
    path('', include('usuarios.urls')),      # Primera página: login
    path('farmacia/', include('farmacia.urls')),  # Dashboard
]
