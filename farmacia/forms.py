# farmacia/forms.py
from django import forms
from .models import Farmacia, Sucursal

class FarmaciaForm(forms.ModelForm):
    # Campos extra relacionados con la sucursal
    sucursal_nombre = forms.CharField(max_length=200, required=False)
    sucursal_direccion = forms.CharField(max_length=300, required=False)
    sucursal_email = forms.EmailField(required=False)

    class Meta:
        model = Farmacia
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Si estamos editando, rellenar campos de la sucursal
        if self.instance and self.instance.pk and self.instance.id_sucursal:
            sucursal = self.instance.id_sucursal
            self.fields['sucursal_nombre'].initial = sucursal.nombre
            self.fields['sucursal_direccion'].initial = sucursal.direccion
            self.fields['sucursal_email'].initial = sucursal.email

    def save(self, commit=True):
        farmacia = super().save(commit=False)

        if commit:
            farmacia.save()

            # Guardar o actualizar la sucursal relacionada
            sucursal = farmacia.id_sucursal
            if sucursal:
                sucursal.nombre = self.cleaned_data.get('sucursal_nombre', sucursal.nombre)
                sucursal.direccion = self.cleaned_data.get('sucursal_direccion', sucursal.direccion)
                sucursal.email = self.cleaned_data.get('sucursal_email', sucursal.email)
                sucursal.save()

        return farmacia
