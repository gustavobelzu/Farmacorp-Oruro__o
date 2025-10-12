from django import forms
from .models import Farmacia

class FarmaciaForm(forms.ModelForm):
    class Meta:
        model = Farmacia
        fields = '__all__'
        widgets = {
            'nombre_farmacia': forms.TextInput(attrs={'class': 'form-control'}),
            'razon_legal': forms.TextInput(attrs={'class': 'form-control'}),
            'id_sucursal': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si es edición (instance existe), bloqueamos el campo nombre_farmacia
        if self.instance and self.instance.pk:
            self.fields['nombre_farmacia'].widget.attrs['readonly'] = True
