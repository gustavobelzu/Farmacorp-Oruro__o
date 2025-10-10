# productos/forms.py
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si es edición (instance existe), bloqueamos el campo código_barra
        if self.instance and self.instance.pk:
            self.fields['codigo_barra'].widget.attrs['readonly'] = True
