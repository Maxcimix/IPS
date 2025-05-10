from django.contrib import admin
from django.utils.html import format_html
from .models import ContactoServicio

@admin.register(ContactoServicio)
class ContactoServicioAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha_inicio_atencion', 'prestador_servicio', 'tipo_atencion_display', 'causa_externa_display', 'diagnostico_principal')
    list_filter = ('ambito_realizacion', 'modalidad_atencion', 'tipo_atencion', 'causa_externa')
    search_fields = ('paciente__primer_nombre', 'paciente__primer_apellido', 'paciente__numero_documento', 'diagnostico_principal')
    date_hierarchy = 'fecha_inicio_atencion'
    
    fieldsets = (
        ('Información del Paciente', {
            'fields': ('paciente',)
        }),
        ('Información de la Atención', {
            'fields': (
                'fecha_inicio_atencion',
                ('prestador_servicio', 'profesional_salud'),
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
        return dict(ContactoServicio.TIPO_ATENCION_CHOICES).get(obj.tipo_atencion)
    tipo_atencion_display.short_description = 'Tipo de Atención'
    
    def causa_externa_display(self, obj):
        return dict(ContactoServicio.CAUSA_EXTERNA_CHOICES).get(obj.causa_externa)
    causa_externa_display.short_description = 'Causa Externa'
    
    class Media:
        css = {
            'all': ('css/admin.css',)
        }
