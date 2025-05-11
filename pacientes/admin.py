# pacientes/admin.py

from django.contrib import admin
from .models import (
    Pais, Departamento, Municipio, TipoDocumento, Discapacidad, 
    ComunidadEtnica, ComunidadIndigena, EntidadAdministradora, 
    Ocupacion, Paciente
)

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre')

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'pais')
    list_filter = ('pais',)
    search_fields = ('codigo', 'nombre')

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'departamento')
    list_filter = ('departamento__pais', 'departamento')
    search_fields = ('codigo', 'nombre')

@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre')

@admin.register(Discapacidad)
class DiscapacidadAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre')

@admin.register(ComunidadEtnica)
class ComunidadEtnicaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre')

@admin.register(ComunidadIndigena)
class ComunidadIndigenaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'comunidad_etnica')
    list_filter = ('comunidad_etnica',)
    search_fields = ('codigo', 'nombre')

@admin.register(EntidadAdministradora)
class EntidadAdministradoraAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'tipo', 'regimen')
    list_filter = ('tipo', 'regimen')
    search_fields = ('codigo', 'nombre')

@admin.register(Ocupacion)
class OcupacionAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'nivel', 'codigo_padre')
    list_filter = ('nivel',)
    search_fields = ('codigo', 'nombre')

class OcupacionInline(admin.TabularInline):
    model = Paciente.ocupaciones.through
    extra = 1

class DiscapacidadInline(admin.TabularInline):
    model = Paciente.discapacidades.through
    extra = 1

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'tipo_documento', 'numero_documento', 'fecha_nacimiento', 'sexo_display', 'telefono', 'entidad_administradora')
    list_filter = ('tipo_documento', 'sexo', 'genero', 'nacionalidad', 'pais_residencia', 'comunidad_etnica', 'zona_residencia')
    search_fields = ('primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'numero_documento')
    inlines = [OcupacionInline, DiscapacidadInline]
    
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
                ('fecha_nacimiento', 'hora_nacimiento'),
                ('sexo', 'genero'),
                'nacionalidad',
                ('comunidad_etnica', 'comunidad_indigena'),
            )
        }),
        ('Información de Residencia', {
            'fields': (
                'pais_residencia',
                ('departamento_residencia', 'municipio_residencia'),
                ('zona_residencia', 'direccion'),
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
            )
        }),
        ('Información Adicional', {
            'fields': (
                ('donante_organos', 'voluntad_anticipada'),
            ),
            'classes': ('collapse',),
        }),
    )
    
    exclude = ('ocupaciones', 'discapacidades')
    
    def nombre_completo(self, obj):
        return obj.nombre_completo()
    nombre_completo.short_description = 'Nombre Completo'
    
    def sexo_display(self, obj):
        return dict(SEXO).get(obj.sexo)
    sexo_display.short_description = 'Sexo'
    
    class Media:
        css = {
            'all': ('css/admin.css',)
        }
