# clientes/forms.py
from django import forms
from .models import Cliente
from empleados.models import Empleado

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['ci_cliente', 'nombre', 'telefono', 'direccion', 'ci_empleado']
        labels = {
            'ci_cliente': 'Cédula',
            'nombre': 'Nombre completo',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
            'ci_empleado': 'Empleado asignado',
        }
        widgets = {
            'ci_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese CI'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese teléfono'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese dirección'}),
            'ci_empleado': forms.Select(attrs={'class': 'form-select'}),
        }
