from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['ci_cliente', 'nombre', 'telefono', 'direccion', 'ci_empleado']
        widgets = {
            'ci_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'ci_empleado': forms.Select(attrs={'class': 'form-select'}),
        }
