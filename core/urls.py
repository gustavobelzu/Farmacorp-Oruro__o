from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),  # Ahora el login será la página principal
    path('farmacia/', include('farmacia.urls')),  # Página principal accesible en /farmacia/
]
