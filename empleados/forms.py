from django import forms
from .models import Empleado, Farmaceutico

class EmpleadoForm(forms.ModelForm):
    # Campos extra para farmacéutico
    matricula = forms.CharField(max_length=50, required=False)
    especialidad = forms.CharField(max_length=50, required=False)

    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
            'fecha_salida': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Bloqueamos CI si es edición
        if self.instance and self.instance.pk:
            self.fields['ci'].widget.attrs['readonly'] = True

        # Si la instancia tiene Farmaceutico relacionado, llenamos los campos extra
        if self.instance.pk:
            try:
                farmaceutico = self.instance.farmaceutico
                self.fields['matricula'].initial = farmaceutico.matricula
                self.fields['especialidad'].initial = farmaceutico.especialidad
            except Farmaceutico.DoesNotExist:
                pass

    def save(self, commit=True):
        # Guardamos primero el empleado
        empleado = super().save(commit)
        # Si se llenó matrícula o especialidad, creamos/actualizamos Farmaceutico
        matricula = self.cleaned_data.get('matricula')
        especialidad = self.cleaned_data.get('especialidad')
        if matricula or especialidad:
            Farmaceutico.objects.update_or_create(
                empleado=empleado,
                defaults={'matricula': matricula, 'especialidad': especialidad}
            )
        return empleado
