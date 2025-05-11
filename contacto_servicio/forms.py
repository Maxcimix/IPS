# contacto_servicio/forms.py

from django import forms
from .models import ContactoServicio

class ContactoServicioForm(forms.ModelForm):
    class Meta:
        model = ContactoServicio
        fields = '__all__'
        widgets = {
            'fecha_inicio_atencion': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_fin_atencion': forms.DateTimeInput(attrs={'type': 'datetime-local', 'required': False}),
            'codigo_tecnologia': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'required': False}),
        }