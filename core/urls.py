from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('farmacia.urls')),  # Esto conecta la ra�z con farmacia
]
