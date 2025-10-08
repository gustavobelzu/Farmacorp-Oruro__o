from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('/farmacia/login/')),  # Redirige "/" a "/farmacia/login/"
    path('farmacia/', include('farmacia.urls')),  # Dashboard y login/logout
    path('productos/', include('productos.urls')),
    # core/urls.py
    path('farmacia/producto/', include('productos.urls')),


]
