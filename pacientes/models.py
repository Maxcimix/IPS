from django.db import models
from django.core.validators import RegexValidator

class Paciente(models.Model):
   
    TIPO_DOCUMENTO = [
        ('CC', 'Cédula de ciudadanía'),
        ('CE', 'Cédula de extranjería'),
        ('CD', 'Carné diplomático'),
        ('PA', 'Pasaporte'),
        ('SC', 'Salvoconducto'),
        ('PE', 'Permiso Especial de Permanencia'),
        ('RC', 'Registro civil'),
        ('TI', 'Tarjeta de identidad'),
        ('CN', 'Certificado de nacido vivo'),
        ('AS', 'Adulto sin identificación'),
        ('MS', 'Menor sin identificación'),
    ]
    
    SEXO = [
        ('01', 'Masculino'),
        ('02', 'Femenino'),
        ('03', 'Indeterminado'),
        ('99', 'No reportado'),
    ]
    
    GENERO = [
        ('01', 'Masculino'),
        ('02', 'Femenino'),
        ('03', 'Transgénero'),
        ('04', 'Neutro'),
        ('05', 'No lo declara'),
    ]
    
    NACIONALIDAD = [
        ('CO', 'Colombia'),
        # Otros países según ISO 3166-1
    ]
    
    ESTADO_DONANTE = [
        ('01', 'Sí'),
        ('02', 'No'),
    ]
    
    VOLUNTAD_ANTICIPADA = [
        ('01', 'Sí'),
        ('02', 'No'),
    ]
    
    DISCAPACIDAD = [
        ('01', 'Física'),
        ('02', 'Mental'),
        ('03', 'Visual'),
        ('04', 'Auditiva'),
        ('05', 'Múltiple'),
        ('06', 'Ninguna'),
        ('99', 'No reportada'),
    ]
    
    PERTENENCIA_ETNICA = [
        ('01', 'Indígena'),
        ('02', 'ROM (Gitano)'),
        ('03', 'Raizal (San Andrés y Providencia)'),
        ('04', 'Palenquero de San Basilio de Palenque'),
        ('05', 'Negro, Mulato, Afrocolombiano o Afrodescendiente'),
        ('06', 'Ninguno de los anteriores'),
    ]
    
    ZONA_RESIDENCIA = [
        ('01', 'Urbana'),
        ('02', 'Rural'),
    ]
    
    
    tipo_documento = models.CharField(max_length=2, choices=TIPO_DOCUMENTO, verbose_name='Tipo de documento')
    numero_documento = models.CharField(max_length=20, verbose_name='Número de documento')
    primer_apellido = models.CharField(max_length=50, verbose_name='Primer apellido')
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True, verbose_name='Segundo apellido')
    primer_nombre = models.CharField(max_length=50, verbose_name='Primer nombre')
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True, verbose_name='Segundo nombre')
    
    
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    sexo = models.CharField(max_length=2, choices=SEXO, verbose_name='Sexo')
    genero = models.CharField(max_length=2, choices=GENERO, verbose_name='Género')
    nacionalidad = models.CharField(max_length=2, choices=NACIONALIDAD, default='CO', verbose_name='Nacionalidad')
    
    
    donante_organos = models.CharField(max_length=2, choices=ESTADO_DONANTE, default='02', verbose_name='Donante de órganos')
    voluntad_anticipada = models.CharField(max_length=2, choices=VOLUNTAD_ANTICIPADA, default='02', verbose_name='Voluntad anticipada')
    
    
    discapacidad = models.CharField(max_length=2, choices=DISCAPACIDAD, default='06', verbose_name='Discapacidad')
    

    pais_residencia = models.CharField(max_length=2, choices=NACIONALIDAD, default='CO', verbose_name='País de residencia')
    departamento_residencia = models.CharField(max_length=2, verbose_name='Departamento de residencia')
    municipio_residencia = models.CharField(max_length=3, verbose_name='Municipio de residencia')
    
    
    pertenencia_etnica = models.CharField(max_length=2, choices=PERTENENCIA_ETNICA, default='06', verbose_name='Pertenencia étnica')
    comunidad_indigena = models.CharField(max_length=100, blank=True, null=True, verbose_name='Comunidad indígena')
    
    
    zona_residencia = models.CharField(max_length=2, choices=ZONA_RESIDENCIA, default='01', verbose_name='Zona de residencia')
    
    
    telefono = models.CharField(max_length=15, validators=[RegexValidator(r'^\d+$', 'Solo se permiten números')], verbose_name='Teléfono')
    email = models.EmailField(blank=True, null=True, verbose_name='Correo electrónico')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    
    
    entidad_administradora = models.CharField(max_length=100, verbose_name='Entidad administradora')
    regimen = models.CharField(max_length=50, verbose_name='Régimen')
    

    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        unique_together = ('tipo_documento', 'numero_documento')
        ordering = ['primer_apellido', 'segundo_apellido', 'primer_nombre', 'segundo_nombre']
    
    def __str__(self):
        return f"{self.primer_apellido} {self.segundo_apellido or ''}, {self.primer_nombre} {self.segundo_nombre or ''} - {self.tipo_documento}: {self.numero_documento}"
    
    def nombre_completo(self):
        return f"{self.primer_nombre} {self.segundo_nombre or ''} {self.primer_apellido} {self.segundo_apellido or ''}"
