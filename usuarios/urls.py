from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.login_view, name='login_root'),  # Para que '' también funcione
]
