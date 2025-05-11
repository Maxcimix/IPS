# contacto_servicio/admin.py

from django.contrib import admin
from .models import (
    ViaIngreso, CausaExterna, TipoTecnologia, DiagnosticoCIE10,
    PrestadorServicio, ProfesionalSalud, ContactoServicio
)

# Admin para modelos de catálogo
@admin.register(ViaIngreso)
class ViaIngresoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre')

@admin.register(CausaExterna)
class CausaExternaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre')

@admin.register(TipoTecnologia)
class TipoTecnologiaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre')

@admin.register(DiagnosticoCIE10)
class DiagnosticoCIE10Admin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'nivel', 'codigo_padre')
    list_filter = ('nivel',)
    search_fields = ('codigo', 'descripcion')

@admin.register(PrestadorServicio)
class PrestadorServicioAdmin(admin.ModelAdmin):
    list_display = ('codigo_habilitacion', 'nombre', 'telefono', 'email')
    search_fields = ('codigo_habilitacion', 'nombre')

@admin.register(ProfesionalSalud)
class ProfesionalSaludAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'especialidad', 'registro_profesional', 'prestador')
    list_filter = ('especialidad', 'prestador')
    search_fields = ('primer_nombre', 'primer_apellido', 'numero_documento')

# Admin para el modelo principal
@admin.register(ContactoServicio)
class ContactoServicioAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha_inicio_atencion', 'prestador', 'profesional', 'tipo_atencion_display', 'causa_externa_display', 'diagnostico_principal')
    list_filter = ('ambito_realizacion', 'modalidad_atencion', 'tipo_atencion', 'causa_externa', 'prestador')
    search_fields = ('paciente__primer_nombre', 'paciente__primer_apellido', 'paciente__numero_documento', 'diagnostico_principal__codigo', 'diagnostico_principal__descripcion')
    date_hierarchy = 'fecha_inicio_atencion'
    
    fieldsets = (
        ('Información del Paciente', {
            'fields': ('paciente',)
        }),
        ('Información de la Atención', {
            'fields': (
                'fecha_inicio_atencion',
                ('prestador', 'profesional'),
                ('ambito_realizacion', 'modalidad_atencion', 'tipo_atencion'),
                'via_ingreso',
                'causa_externa',
            )
        }),
        ('Información Clínica', {
            'fields': (
                'clasificacion_triage',
                ('diagnostico_principal', 'tipo_diagnostico'),
                ('tipo_tecnologia', 'codigo_tecnologia'),
            )
        }),
        ('Finalización y Observaciones', {
            'fields': (
                'fecha_fin_atencion',
                'observaciones',
            )
        }),
    )
    
    def tipo_atencion_display(self, obj):
        return dict(TIPO_ATENCION).get(obj.tipo_atencion)
    tipo_atencion_display.short_description = 'Tipo de Atención'
    
    def causa_externa_display(self, obj):
        return obj.causa_externa.nombre
    causa_externa_display.short_description = 'Causa Externa'
    
    class Media:
        css = {
            'all': ('css/admin.css',)
        }