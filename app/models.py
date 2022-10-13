# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from distutils.command.upload import upload
from django.db import models


class Boleta(models.Model): 
    id_boleta = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    monto = models.IntegerField(blank=True, null=True)
    paciente_rut_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='paciente_rut_paciente')

    class Meta:
        managed = False
        db_table = 'boleta'


class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.DateField()
    lugar = models.CharField(max_length=20, blank=True, null=True)
    paciente_rut_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='paciente_rut_paciente')
    especialista_rut_especialista = models.ForeignKey('Especialista', models.DO_NOTHING, db_column='especialista_rut_especialista')

    class Meta:
        managed = False
        db_table = 'cita'
        unique_together = (('id_cita', 'paciente_rut_paciente', 'especialista_rut_especialista'),)


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    desc_comuna = models.CharField(max_length=20)
    region_id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_id_region')

    class Meta:
        managed = False
        db_table = 'comuna'


class Consultas(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=2)
    correo = models.CharField(max_length=30)
    telefono = models.IntegerField()
    mensaje = models.CharField(max_length=500)
    paciente_rut_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='paciente_rut_paciente')

    class Meta:
        managed = False
        db_table = 'consultas'


class Convenio(models.Model):
    id_convenio = models.IntegerField(primary_key=True)
    nombre_convenio = models.CharField(max_length=30)
    descuento = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'convenio'


class Especialidad(models.Model):
    id_especialidad = models.IntegerField(primary_key=True)
    desc_especialidad = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'especialidad'


class Especialista(models.Model):
    rut_especialista = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_p = models.CharField(max_length=20)
    apellido_m = models.CharField(max_length=20)
    correo = models.CharField(max_length=30)
    telefono = models.IntegerField()
    imagen = models.ImageField(upload_to="especialistas" ,blank=True, null=True )
    region_id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_id_region')
    especialidad_id_especialidad = models.ForeignKey(Especialidad, models.DO_NOTHING, db_column='especialidad_id_especialidad')
    tipo_titulo_id_titulo = models.ForeignKey('TipoTitulo', models.DO_NOTHING, db_column='tipo_titulo_id_titulo')

    class Meta:
        managed = False
        db_table = 'especialista'


class FichaAtencion(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    fecha = models.DateField()
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    motivo_consulta = models.CharField(max_length=500, blank=True, null=True)
    especialista_rut_especialista = models.ForeignKey(Especialista, models.DO_NOTHING, db_column='especialista_rut_especialista')
    paciente_rut_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='paciente_rut_paciente')

    class Meta:
        managed = False
        db_table = 'ficha_atencion'


class Paciente(models.Model):
    rut_paciente = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_p = models.CharField(max_length=20)
    apellido_m = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    correo = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=20)
    telefono = models.IntegerField()
    contrasenia = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1)
    profesion = models.CharField(max_length=20, blank=True, null=True)
    convenio_id_convenio = models.ForeignKey(Convenio, models.DO_NOTHING, db_column='convenio_id_convenio')
    prevision_id_prevision = models.ForeignKey('Prevision', models.DO_NOTHING, db_column='prevision_id_prevision')

    class Meta:
        managed = False
        db_table = 'paciente'


class Prevision(models.Model):
    id_prevision = models.IntegerField(primary_key=True)
    desc_prevision = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'prevision'


class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    desc_region = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'region'


class Taller(models.Model):
    id_taller = models.IntegerField(primary_key=True)
    nombre_taller = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    imagen = models.ImageField(upload_to="talleres" ,blank=True ,null=True)
    precio = models.IntegerField(blank=True, null=True)
    especialista_rut_especialista = models.ForeignKey(Especialista, models.DO_NOTHING, db_column='especialista_rut_especialista')

    class Meta:
        managed = False
        db_table = 'taller'


class TipoTitulo(models.Model):
    id_titulo = models.IntegerField(primary_key=True)
    desc_titulo = models.CharField(max_length=30)
    universidad = models.CharField(max_length=30)
    annio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_titulo'


class Tutor(models.Model):
    rut_tutor = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellidio_p = models.CharField(max_length=20)
    apellido_m = models.CharField(max_length=20)
    correo = models.CharField(max_length=30)
    telefono = models.IntegerField()
    contrasenia = models.CharField(max_length=20)
    paciente_rut_paciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='paciente_rut_paciente')

    class Meta:
        managed = False
        db_table = 'tutor'


class UsuariosAdmin(models.Model):
    id_admin = models.IntegerField(primary_key=True)
    nombre_admin = models.CharField(max_length=40)
    correo_admin = models.CharField(max_length=30)
    contrasenia = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'usuarios_admin'
