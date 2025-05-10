
from django.db import migrations, models
import django.core.validators

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('CE', 'Cédula de extranjería'), ('CD', 'Carné diplomático'), ('PA', 'Pasaporte'), ('SC', 'Salvoconducto'), ('PE', 'Permiso Especial de Permanencia'), ('RC', 'Registro civil'), ('TI', 'Tarjeta de identidad'), ('CN', 'Certificado de nacido vivo'), ('AS', 'Adulto sin identificación'), ('MS', 'Menor sin identificación')], max_length=2, verbose_name='Tipo de documento')),
                ('numero_documento', models.CharField(max_length=20, verbose_name='Número de documento')),
                ('primer_apellido', models.CharField(max_length=50, verbose_name='Primer apellido')),
                ('segundo_apellido', models.CharField(blank=True, max_length=50, null=True, verbose_name='Segundo apellido')),
                ('primer_nombre', models.CharField(max_length=50, verbose_name='Primer nombre')),
                ('segundo_nombre', models.CharField(blank=True, max_length=50, null=True, verbose_name='Segundo nombre')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('sexo', models.CharField(choices=[('01', 'Masculino'), ('02', 'Femenino'), ('03', 'Indeterminado'), ('99', 'No reportado')], max_length=2, verbose_name='Sexo')),
                ('genero', models.CharField(choices=[('01', 'Masculino'), ('02', 'Femenino'), ('03', 'Transgénero'), ('04', 'Neutro'), ('05', 'No lo declara')], max_length=2, verbose_name='Género')),
                ('nacionalidad', models.CharField(choices=[('CO', 'Colombia')], default='CO', max_length=2, verbose_name='Nacionalidad')),
                ('donante_organos', models.CharField(choices=[('01', 'Sí'), ('02', 'No')], default='02', max_length=2, verbose_name='Donante de órganos')),
                ('voluntad_anticipada', models.CharField(choices=[('01', 'Sí'), ('02', 'No')], default='02', max_length=2, verbose_name='Voluntad anticipada')),
                ('discapacidad', models.CharField(choices=[('01', 'Física'), ('02', 'Mental'), ('03', 'Visual'), ('04', 'Auditiva'), ('05', 'Múltiple'), ('06', 'Ninguna'), ('99', 'No reportada')], default='06', max_length=2, verbose_name='Discapacidad')),
                ('pais_residencia', models.CharField(choices=[('CO', 'Colombia')], default='CO', max_length=2, verbose_name='País de residencia')),
                ('departamento_residencia', models.CharField(max_length=2, verbose_name='Departamento de residencia')),
                ('municipio_residencia', models.CharField(max_length=3, verbose_name='Municipio de residencia')),
                ('pertenencia_etnica', models.CharField(choices=[('01', 'Indígena'), ('02', 'ROM (Gitano)'), ('03', 'Raizal (San Andrés y Providencia)'), ('04', 'Palenquero de San Basilio de Palenque'), ('05', 'Negro, Mulato, Afrocolombiano o Afrodescendiente'), ('06', 'Ninguno de los anteriores')], default='06', max_length=2, verbose_name='Pertenencia étnica')),
                ('comunidad_indigena', models.CharField(blank=True, max_length=100, null=True, verbose_name='Comunidad indígena')),
                ('zona_residencia', models.CharField(choices=[('01', 'Urbana'), ('02', 'Rural')], default='01', max_length=2, verbose_name='Zona de residencia')),
                ('telefono', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\d+$', 'Solo se permiten números')], verbose_name='Teléfono')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo electrónico')),
                ('direccion', models.CharField(max_length=255, verbose_name='Dirección')),
                ('entidad_administradora', models.CharField(max_length=100, verbose_name='Entidad administradora')),
                ('regimen', models.CharField(max_length=50, verbose_name='Régimen')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'ordering': ['primer_apellido', 'segundo_apellido', 'primer_nombre', 'segundo_nombre'],
                'unique_together': {('tipo_documento', 'numero_documento')},
            },
        ),
    ]
