from django.urls import path
from . import views

app_name = 'usuarios'  # ✅ Esto es clave para el namespace

urlpatterns = [
    path('login/', views.login_view, name='login'),   # <- name='login'
    path('logout/', views.logout_view, name='logout'),
]
