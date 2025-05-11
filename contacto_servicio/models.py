# contacto_servicio/models.py

from django.db import models
from pacientes.models import Paciente

# Enumeraciones (menos de 5 opciones)
AMBITO_REALIZACION = [
    ('01', 'Ambulatorio'),
    ('02', 'Hospitalario'),
    ('03', 'Urgencias'),
    ('04', 'Domiciliario'),
    ('05', 'Extramural Jornada de Salud'),
]

MODALIDAD_ATENCION = [
    ('01', 'Intramural'),
    ('02', 'Extramural'),
    ('03', 'Telemedicina'),
]

TIPO_ATENCION = [
    ('01', 'Consulta externa'),
    ('02', 'Servicio de urgencias'),
    ('03', 'Hospitalización'),
    ('04', 'Quirúrgico'),
    ('05', 'Atención Inmediata'),
]

CLASIFICACION_TRIAGE = [
    ('1', 'Triage I'),
    ('2', 'Triage II'),
    ('3', 'Triage III'),
    ('4', 'Triage IV'),
    ('5', 'Triage V'),
]

TIPO_DIAGNOSTICO = [
    ('01', 'Impresión diagnóstica'),
    ('02', 'Confirmado nuevo'),
    ('03', 'Confirmado repetido'),
]

# Modelos para campos con más de 5 opciones
class ViaIngreso(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Vía de Ingreso'
        verbose_name_plural = 'Vías de Ingreso'
        ordering = ['codigo']
    
    def __str__(self):
        return self.nombre

class CausaExterna(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Causa Externa'
        verbose_name_plural = 'Causas Externas'
        ordering = ['codigo']
    
    def __str__(self):
        return self.nombre

class TipoTecnologia(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Tipo de Tecnología'
        verbose_name_plural = 'Tipos de Tecnología'
        ordering = ['codigo']
    
    def __str__(self):
        return self.nombre

class DiagnosticoCIE10(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    descripcion = models.CharField(max_length=255)
    codigo_padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='hijos')
    nivel = models.IntegerField()
    
    class Meta:
        verbose_name = 'Diagnóstico CIE-10'
        verbose_name_plural = 'Diagnósticos CIE-10'
        ordering = ['codigo']
    
    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"

class PrestadorServicio(models.Model):
    codigo_habilitacion = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    tipo_prestador = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Prestador de Servicio'
        verbose_name_plural = 'Prestadores de Servicio'
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre} ({self.codigo_habilitacion})"

class ProfesionalSalud(models.Model):
    tipo_documento = models.CharField(max_length=2)
    numero_documento = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True)
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True)
    especialidad = models.CharField(max_length=100)
    registro_profesional = models.CharField(max_length=50)
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.PROTECT, related_name='profesionales',null=True, blank=True)
    
    class Meta:
        verbose_name = 'Profesional de Salud'
        verbose_name_plural = 'Profesionales de Salud'
        ordering = ['primer_apellido', 'primer_nombre']
        unique_together = ('tipo_documento', 'numero_documento')
    
    def __str__(self):
        return f"{self.primer_apellido} {self.primer_nombre} - {self.especialidad}"
    
    def nombre_completo(self):
        return f"{self.primer_nombre} {self.segundo_nombre or ''} {self.primer_apellido} {self.segundo_apellido or ''}"

# Modelo principal de Contacto con Servicio de Salud
class ContactoServicio(models.Model):
    # Relación con Paciente
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='contactos_servicio', verbose_name='Paciente')
    
    # Relaciones con modelos de catálogo
    prestador = models.ForeignKey(PrestadorServicio, on_delete=models.PROTECT, related_name='contactos_servicio', verbose_name='Prestador de servicio')
    profesional = models.ForeignKey(ProfesionalSalud, on_delete=models.PROTECT, related_name='contactos_servicio', verbose_name='Profesional de salud')
    via_ingreso = models.ForeignKey(ViaIngreso, on_delete=models.PROTECT, verbose_name='Vía de ingreso')
    causa_externa = models.ForeignKey(CausaExterna, on_delete=models.PROTECT, verbose_name='Causa externa')
    diagnostico_principal = models.ForeignKey(DiagnosticoCIE10, on_delete=models.PROTECT, related_name='contactos_servicio', verbose_name='Diagnóstico principal')
    tipo_tecnologia = models.ForeignKey(TipoTecnologia, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Tipo de tecnología')
    
    # Campos con enumeraciones (menos de 5 opciones)
    ambito_realizacion = models.CharField(max_length=2, choices=AMBITO_REALIZACION, verbose_name='Ámbito de realización')
    modalidad_atencion = models.CharField(max_length=2, choices=MODALIDAD_ATENCION, verbose_name='Modalidad de atención')
    tipo_atencion = models.CharField(max_length=2, choices=TIPO_ATENCION, verbose_name='Tipo de atención')
    clasificacion_triage = models.CharField(max_length=1, choices=CLASIFICACION_TRIAGE, blank=True, null=True, verbose_name='Clasificación Triage')
    tipo_diagnostico = models.CharField(max_length=2, choices=TIPO_DIAGNOSTICO, verbose_name='Tipo de diagnóstico')
    
    # Otros campos
    fecha_inicio_atencion = models.DateTimeField(verbose_name='Fecha y hora de inicio de atención')
    fecha_fin_atencion = models.DateTimeField(verbose_name='Fecha y hora de fin de atención', null=True, blank=True)
    codigo_tecnologia = models.CharField(max_length=20, blank=True, null=True, verbose_name='Código de tecnología')
    observaciones = models.TextField(blank=True, null=True, verbose_name='Observaciones')
    
    # Campos de auditoría
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    class Meta:
        verbose_name = 'Contacto con Servicio de Salud'
        verbose_name_plural = 'Contactos con Servicio de Salud'
        ordering = ['-fecha_inicio_atencion']
    
    def __str__(self):
        return f"Atención a {self.paciente} - {self.fecha_inicio_atencion.strftime('%d/%m/%Y %H:%M')}"