# farmacia/forms_sucursal.py
from django import forms
from .models import Sucursal

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = '__all__'
        widgets = {
            'fecha_registro': forms.DateInput(attrs={'type': 'date'}),
            'email': forms.EmailInput(attrs={'placeholder': 'correo@dominio.com'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Bloquear NIT si es edición
        if self.instance and self.instance.pk:
            self.fields['nit'].widget.attrs['readonly'] = True
