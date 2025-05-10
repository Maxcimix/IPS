from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento_residencia': forms.TextInput(attrs={'class': 'form-control'}),
            'municipio_residencia': forms.TextInput(attrs={'class': 'form-control'}),
            'comunidad_indigena': forms.TextInput(attrs={'class': 'form-control'}),
            'entidad_administradora': forms.TextInput(attrs={'class': 'form-control'}),
            'regimen': forms.TextInput(attrs={'class': 'form-control'}),
        }
