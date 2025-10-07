from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='farmacia_inicio'),  # Vista principal de farmacia
]
