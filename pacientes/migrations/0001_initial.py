# Generated by Django 5.2 on 2025-05-11 03:43

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComunidadEtnica',
            fields=[
                ('codigo', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Comunidad Étnica',
                'verbose_name_plural': 'Comunidades Étnicas',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('codigo', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Discapacidad',
            fields=[
                ('codigo', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Discapacidad',
                'verbose_name_plural': 'Discapacidades',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='EntidadAdministradora',
            fields=[
                ('codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=50)),
                ('regimen', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Entidad Administradora',
                'verbose_name_plural': 'Entidades Administradoras',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('codigo', models.CharField(max_length=3, primary_key=True, serialize=False, verbose_name='Código')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Países',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('codigo', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tipo de Documento',
                'verbose_name_plural': 'Tipos de Documento',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='ComunidadIndigena',
            fields=[
                ('codigo', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('comunidad_etnica', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comunidades_indigenas', to='pacientes.comunidadetnica')),
            ],
            options={
                'verbose_name': 'Comunidad Indígena',
                'verbose_name_plural': 'Comunidades Indígenas',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('codigo', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='municipios', to='pacientes.departamento')),
            ],
            options={
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'Municipios',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('nivel', models.IntegerField()),
                ('codigo_padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hijos', to='pacientes.ocupacion')),
            ],
            options={
                'verbose_name': 'Ocupación',
                'verbose_name_plural': 'Ocupaciones',
                'ordering': ['codigo'],
            },
        ),
        migrations.AddField(
            model_name='departamento',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='departamentos', to='pacientes.pais'),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_documento', models.CharField(max_length=20, verbose_name='Número de documento')),
                ('primer_apellido', models.CharField(max_length=50, verbose_name='Primer apellido')),
                ('segundo_apellido', models.CharField(blank=True, max_length=50, null=True, verbose_name='Segundo apellido')),
                ('primer_nombre', models.CharField(max_length=50, verbose_name='Primer nombre')),
                ('segundo_nombre', models.CharField(blank=True, max_length=50, null=True, verbose_name='Segundo nombre')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('hora_nacimiento', models.TimeField(blank=True, null=True, verbose_name='Hora de nacimiento')),
                ('sexo', models.CharField(choices=[('01', 'Masculino'), ('02', 'Femenino'), ('03', 'Indeterminado'), ('99', 'No reportado')], max_length=2, verbose_name='Sexo')),
                ('genero', models.CharField(choices=[('01', 'Masculino'), ('02', 'Femenino'), ('03', 'Transgénero'), ('04', 'Neutro'), ('05', 'No lo declara')], max_length=2, verbose_name='Género')),
                ('zona_residencia', models.CharField(choices=[('01', 'Urbana'), ('02', 'Rural')], default='01', max_length=2, verbose_name='Zona de residencia')),
                ('direccion', models.CharField(max_length=255, verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\d+$', 'Solo se permiten números')], verbose_name='Teléfono')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo electrónico')),
                ('donante_organos', models.CharField(choices=[('01', 'Sí'), ('02', 'No')], default='02', max_length=2, verbose_name='Donante de órganos')),
                ('voluntad_anticipada', models.CharField(choices=[('01', 'Sí'), ('02', 'No')], default='02', max_length=2, verbose_name='Voluntad anticipada')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('comunidad_etnica', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pacientes.comunidadetnica', verbose_name='Comunidad étnica')),
                ('comunidad_indigena', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pacientes.comunidadindigena', verbose_name='Comunidad indígena')),
                ('departamento_residencia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pacientes_residentes', to='pacientes.departamento', verbose_name='Departamento de residencia')),
                ('discapacidades', models.ManyToManyField(blank=True, to='pacientes.discapacidad', verbose_name='Discapacidades')),
                ('entidad_administradora', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pacientes.entidadadministradora', verbose_name='Entidad administradora')),
                ('municipio_residencia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pacientes_residentes', to='pacientes.municipio', verbose_name='Municipio de residencia')),
                ('ocupaciones', models.ManyToManyField(blank=True, to='pacientes.ocupacion', verbose_name='Ocupaciones')),
                ('nacionalidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pacientes_por_nacionalidad', to='pacientes.pais', verbose_name='Nacionalidad')),
                ('pais_residencia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pacientes_residentes', to='pacientes.pais', verbose_name='País de residencia')),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pacientes.tipodocumento', verbose_name='Tipo de documento')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'ordering': ['primer_apellido', 'segundo_apellido', 'primer_nombre', 'segundo_nombre'],
                'unique_together': {('tipo_documento', 'numero_documento')},
            },
        ),
    ]
