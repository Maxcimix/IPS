# pacientes/models.py

from django.db import models
from django.core.validators import RegexValidator

# Enumeraciones (menos de 5 opciones)
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

ZONA_RESIDENCIA = [
    ('01', 'Urbana'),
    ('02', 'Rural'),
]

ESTADO_DONANTE = [
    ('01', 'Sí'),
    ('02', 'No'),
]

VOLUNTAD_ANTICIPADA = [
    ('01', 'Sí'),
    ('02', 'No'),
]

class Pais(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True, verbose_name='Código')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    
    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, related_name='departamentos')
    
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)  # Código DANE completo
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, related_name='municipios')
    
    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class TipoDocumento(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documento'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class Discapacidad(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Discapacidad'
        verbose_name_plural = 'Discapacidades'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class ComunidadEtnica(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Comunidad Étnica'
        verbose_name_plural = 'Comunidades Étnicas'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class ComunidadIndigena(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=100)
    comunidad_etnica = models.ForeignKey(ComunidadEtnica, on_delete=models.PROTECT, related_name='comunidades_indigenas')
    
    class Meta:
        verbose_name = 'Comunidad Indígena'
        verbose_name_plural = 'Comunidades Indígenas'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class EntidadAdministradora(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50)  # EPS, ARL, etc.
    regimen = models.CharField(max_length=50)  # Contributivo, Subsidiado, etc.
    
    class Meta:
        verbose_name = 'Entidad Administradora'
        verbose_name_plural = 'Entidades Administradoras'
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre} ({self.tipo} - {self.regimen})"

class Ocupacion(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=255)
    codigo_padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='hijos')
    nivel = models.IntegerField()
    
    class Meta:
        verbose_name = 'Ocupación'
        verbose_name_plural = 'Ocupaciones'
        ordering = ['codigo']
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

# Modelo principal de Paciente
class Paciente(models.Model):
    # Campos de identificación
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT, verbose_name='Tipo de documento')
    numero_documento = models.CharField(max_length=20, verbose_name='Número de documento')
    primer_apellido = models.CharField(max_length=50, verbose_name='Primer apellido')
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True, verbose_name='Segundo apellido')
    primer_nombre = models.CharField(max_length=50, verbose_name='Primer nombre')
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True, verbose_name='Segundo nombre')
    
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    hora_nacimiento = models.TimeField(verbose_name='Hora de nacimiento', null=True, blank=True)
    sexo = models.CharField(max_length=2, choices=SEXO, verbose_name='Sexo')
    genero = models.CharField(max_length=2, choices=GENERO, verbose_name='Género')
    
    nacionalidad = models.ForeignKey(Pais, on_delete=models.PROTECT, related_name='pacientes_por_nacionalidad', verbose_name='Nacionalidad')
    pais_residencia = models.ForeignKey(Pais, on_delete=models.PROTECT, related_name='pacientes_residentes', verbose_name='País de residencia')
    departamento_residencia = models.ForeignKey(Departamento, on_delete=models.PROTECT, related_name='pacientes_residentes', verbose_name='Departamento de residencia')
    municipio_residencia = models.ForeignKey(Municipio, on_delete=models.PROTECT, related_name='pacientes_residentes', verbose_name='Municipio de residencia')
    zona_residencia = models.CharField(max_length=2, choices=ZONA_RESIDENCIA, default='01', verbose_name='Zona de residencia')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    

    telefono = models.CharField(max_length=15, validators=[RegexValidator(r'^\d+$', 'Solo se permiten números')], verbose_name='Teléfono')
    email = models.EmailField(blank=True, null=True, verbose_name='Correo electrónico')
    
    # Campos de pertenencia étnica
    comunidad_etnica = models.ForeignKey(ComunidadEtnica, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Comunidad étnica')
    comunidad_indigena = models.ForeignKey(ComunidadIndigena, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Comunidad indígena')
    

    entidad_administradora = models.ForeignKey(EntidadAdministradora, on_delete=models.PROTECT, verbose_name='Entidad administradora')
    

    donante_organos = models.CharField(max_length=2, choices=ESTADO_DONANTE, default='02', verbose_name='Donante de órganos')
    voluntad_anticipada = models.CharField(max_length=2, choices=VOLUNTAD_ANTICIPADA, default='02', verbose_name='Voluntad anticipada')
    
    ocupaciones = models.ManyToManyField(Ocupacion, blank=True, verbose_name='Ocupaciones')
    discapacidades = models.ManyToManyField(Discapacidad, blank=True, verbose_name='Discapacidades')
    
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