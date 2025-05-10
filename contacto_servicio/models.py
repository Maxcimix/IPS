from django.db import models
from pacientes.models import Paciente

class ContactoServicio(models.Model):
    
    AMBITO_REALIZACION_CHOICES = [
        ('01', 'Ambulatorio'),
        ('02', 'Hospitalario'),
        ('03', 'Urgencias'),
        ('04', 'Domiciliario'),
        ('05', 'Extramural Jornada de Salud'),
        ('06', 'Extramural Unidad Móvil'),
        ('07', 'Telemedicina no interactiva'),
        ('08', 'Telemedicina-Telexperticia'),
        ('09', 'Telemedicina-Teleorientación'),
    ]
    
    MODALIDAD_ATENCION_CHOICES = [
        ('01', 'Intramural'),
        ('02', 'Extramural'),
        ('03', 'Telemedicina'),
    ]
    
    TIPO_ATENCION_CHOICES = [
        ('01', 'Consulta externa'),
        ('02', 'Servicio de urgencias'),
        ('03', 'Hospitalización'),
        ('04', 'Quirúrgico'),
        ('05', 'Atención Inmediata'),
    ]
    
    VIA_INGRESO_CHOICES = [
        ('01', 'Consulta externa'),
        ('02', 'Remisión externa'),
        ('03', 'Servicio de urgencias'),
        ('04', 'Derivado de hospitalización'),
        ('05', 'Derivado de sala de cirugía'),
        ('06', 'Derivado de sala de partos'),
        ('07', 'Recién nacido en la institución'),
        ('08', 'Derivado de atención domiciliaria'),
        ('09', 'Derivado de telemedicina'),
        ('10', 'Derivado de otro servicio de salud'),
        ('11', 'Referido'),
    ]
    
    CAUSA_EXTERNA_CHOICES = [
        ('01', 'Enfermedad general de origen común'),
        ('02', 'Accidente de tránsito'),
        ('03', 'Accidente de origen laboral'),
        ('04', 'Accidente en el hogar'),
        ('05', 'Evento de origen natural'),
        ('06', 'Lesión por agresión'),
        ('07', 'Lesión auto infligida'),
        ('08', 'Sospecha de violencia física'),
        ('09', 'Sospecha de violencia psicológica'),
        ('10', 'Sospecha de violencia sexual'),
        ('11', 'Sospecha de negligencia y abandono'),
        ('12', 'IVE relacionado con peligro a la salud o vida de la mujer'),
        ('13', 'IVE por malformación congénita incompatible con la vida'),
        ('14', 'IVE por violencia sexual, incesto o por inseminación artificial o transferencia de ovulo fecundado no consentida'),
        ('15', 'Evento adverso en salud'),
        ('16', 'Enfermedad general'),
        ('17', 'Enfermedad laboral'),
        ('18', 'Promoción y mantenimiento de la salud-Intervenciones individuales'),
        ('19', 'Eventos Catastróficos'),
        ('20', 'Accidente de mina antipersonal-MAP'),
        ('21', 'Accidente de Artefacto Explosivo Improvisado -AEI'),
        ('22', 'Accidente de Munición Sin Explotar-MUSE'),
        ('23', 'Otra víctima de conflicto armado colombiano'),
    ]
    
    CLASIFICACION_TRIAGE_CHOICES = [
        ('1', 'Triage I'),
        ('2', 'Triage II'),
        ('3', 'Triage III'),
        ('4', 'Triage IV'),
        ('5', 'Triage V'),
    ]
    
    TIPO_DIAGNOSTICO_CHOICES = [
        ('01', 'Impresión diagnóstica'),
        ('02', 'Confirmado nuevo'),
        ('03', 'Confirmado repetido'),
    ]
    
    TIPO_TECNOLOGIA_CHOICES = [
        ('01', 'Procedimiento en salud'),
        ('02', 'Medicamento con registro sanitario'),
        ('03', 'Medicamento vital no disponible'),
        ('04', 'Preparación magistral'),
        ('05', 'Medicamento no incluido'),
        ('06', 'Componentes sanguíneos'),
        ('07', 'Fluidos orgánicos'),
        ('08', 'Órganos'),
        ('09', 'Tejidos'),
        ('10', 'Células'),
        ('11', 'Producto nutricional'),
        ('12', 'Servicio complementario'),
    ]
    
   
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='contactos_servicio', verbose_name='Paciente')
    
    
    fecha_inicio_atencion = models.DateTimeField(verbose_name='Fecha y hora de inicio de atención')
    prestador_servicio = models.CharField(max_length=100, verbose_name='Prestador del servicio')
    profesional_salud = models.CharField(max_length=100, verbose_name='Profesional de salud')
    
    
    ambito_realizacion = models.CharField(max_length=2, choices=AMBITO_REALIZACION_CHOICES, verbose_name='Ámbito de realización')
    modalidad_atencion = models.CharField(max_length=2, choices=MODALIDAD_ATENCION_CHOICES, verbose_name='Modalidad de atención')
    tipo_atencion = models.CharField(max_length=2, choices=TIPO_ATENCION_CHOICES, verbose_name='Tipo de atención')
    
    
    via_ingreso = models.CharField(max_length=2, choices=VIA_INGRESO_CHOICES, verbose_name='Vía de ingreso')
    causa_externa = models.CharField(max_length=2, choices=CAUSA_EXTERNA_CHOICES, verbose_name='Causa externa')
    
    
    clasificacion_triage = models.CharField(max_length=1, choices=CLASIFICACION_TRIAGE_CHOICES, blank=True, null=True, verbose_name='Clasificación Triage')
    diagnostico_principal = models.CharField(max_length=10, verbose_name='Diagnóstico principal (CIE-10)')
    tipo_diagnostico = models.CharField(max_length=2, choices=TIPO_DIAGNOSTICO_CHOICES, verbose_name='Tipo de diagnóstico')
    
    
    tipo_tecnologia = models.CharField(max_length=2, choices=TIPO_TECNOLOGIA_CHOICES, blank=True, null=True, verbose_name='Tipo de tecnología')
    codigo_tecnologia = models.CharField(max_length=20, blank=True, null=True, verbose_name='Código de tecnología')
    
    
    fecha_fin_atencion = models.DateTimeField(blank=True, null=True, verbose_name='Fecha y hora de fin de atención')
    
    
    observaciones = models.TextField(blank=True, null=True, verbose_name='Observaciones')
    
   
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    class Meta:
        verbose_name = 'Contacto con Servicio de Salud'
        verbose_name_plural = 'Contactos con Servicio de Salud'
        ordering = ['-fecha_inicio_atencion']
    
    def __str__(self):
        return f"Atención a {self.paciente} - {self.fecha_inicio_atencion.strftime('%d/%m/%Y %H:%M')}"
