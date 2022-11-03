# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models.deletion import SET_DEFAULT
from django.db.models.fields import NullBooleanField



class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    nombre_region = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.nombre_region


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nombre_comuna = models.CharField(max_length=30, null=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.nombre_comuna

class Titulo(models.Model):
    nombre_titulo = models.CharField(max_length=40)
    universidad = models.CharField(max_length=40)
    annio_egreso = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre_titulo


class Convenio(models.Model):
    id_convenio = models.IntegerField(primary_key=True)
    nombre_convenio = models.CharField(max_length=30, null=True)
    descuento = models.IntegerField()

    def __str__(self):
        return self.nombre_convenio

class Prevision(models.Model):
    id_prevision = models.IntegerField(primary_key=True)
    nombre_prevision = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.nombre_prevision


class Especialidad(models.Model):
    id_especialidad = models.IntegerField(primary_key=True)
    nombre_especialidad = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.nombre_especialidad


class Especialista(models.Model):
    rut_especialista = models.CharField(primary_key=True, max_length=15)
    dv = models.CharField(max_length=1, null=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, null=True)
    correo = models.CharField(max_length=40)
    telefono = models.IntegerField(null=True)
    precio_consulta = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="especialistas" ,blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT, null=True)
    tipo_titulo = models.ForeignKey(Titulo, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.nombre



class Paciente(models.Model):
    rut_paciente = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50, null=True)
    fecha_nacimiento = models.DateField()
    correo = models.CharField(max_length=40)
    telefono = models.IntegerField()
    contrasenia = models.CharField(max_length=20,)
    sexo = models.CharField(max_length=1, null=True)
    convenio = models.ForeignKey(Convenio, on_delete=models.PROTECT, null=True)
    prevision = models.ForeignKey(Prevision, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.rut_paciente



class FichaAtencion(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    fecha = models.DateField(null=True)
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    motivo_consulta = models.CharField(max_length=500, blank=True, null=True)
    especialista = models.ForeignKey(Especialista, on_delete=models.PROTECT, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return str(self.id_ficha)#self.id_ficha


class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    fecha = models.DateField(null=True)
    hora = models.IntegerField(null=True)
    lugar = models.CharField(max_length=30, blank=True, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, null=True)
    especialista = models.ForeignKey(Especialista, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return str(self.id_cita)


opciones_consulta = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "devolución"]
]

class Consultas(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=2, null=True)
    correo = models.CharField(max_length=30, null=True)
    telefono = models.IntegerField(null=True)
    opciones_consulta = models.IntegerField(choices=opciones_consulta, null=True)
    mensaje = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.id_consulta


class Taller(models.Model):
    id_taller = models.IntegerField(primary_key=True)
    nombre_taller = models.CharField(max_length=50, null=True)
    descripcion = models.CharField(max_length=300, blank=True, null=True)
    imagen = models.ImageField(upload_to="talleres" ,blank=True ,null=True)
    precio = models.IntegerField(blank=True, null=True)
    especialista = models.ForeignKey(Especialista, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.nombre_taller

class Boleta(models.Model): 
    id_boleta = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    monto = models.IntegerField(blank=True, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.id_boleta


class Tutor(models.Model):
    rut_tutor = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=50, null=True)
    apellido = models.CharField(max_length=50, null=True)
    correo = models.CharField(max_length=50, null=True)
    telefono = models.IntegerField(null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.rut_tutor

