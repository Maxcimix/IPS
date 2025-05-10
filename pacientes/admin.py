from django.contrib import admin
from django.utils.html import format_html
from .models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo_display', 'tipo_documento', 'numero_documento', 'fecha_nacimiento', 'sexo_display', 'telefono', 'entidad_administradora')
    list_filter = ('tipo_documento', 'sexo', 'genero', 'pertenencia_etnica', 'zona_residencia')
    search_fields = ('primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'numero_documento')
    fieldsets = (
        ('Información de Identificación', {
            'fields': (
                ('tipo_documento', 'numero_documento'),
                ('primer_apellido', 'segundo_apellido'),
                ('primer_nombre', 'segundo_nombre'),
            )
        }),
        ('Información Demográfica', {
            'fields': (
                'fecha_nacimiento',
                ('sexo', 'genero'),
                'nacionalidad',
                ('pertenencia_etnica', 'comunidad_indigena'),
            )
        }),
        ('Información de Residencia', {
            'fields': (
                ('pais_residencia', 'zona_residencia'),
                ('departamento_residencia', 'municipio_residencia'),
                'direccion',
            )
        }),
        ('Información de Contacto', {
            'fields': (
                'telefono',
                'email',
            )
        }),
        ('Información de Aseguramiento', {
            'fields': (
                'entidad_administradora',
                'regimen',
            )
        }),
        ('Información Adicional', {
            'fields': (
                ('donante_organos', 'voluntad_anticipada'),
                'discapacidad',
            ),
            'classes': ('collapse',),
        }),
    )
    
    def nombre_completo_display(self, obj):
        return obj.nombre_completo()
    nombre_completo_display.short_description = 'Nombre Completo'
    
    def sexo_display(self, obj):
        return dict(Paciente.SEXO_CHOICES).get(obj.sexo)
    sexo_display.short_description = 'Sexo'
    
    class Media:
        css = {
            'all': ('css/admin.css',)
        }
