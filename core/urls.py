from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('farmacia.urls')), # Página principal
    path('usuarios/', include('usuarios.urls')), # Login
]
