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
from django.contrib.auth.models import User 
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.core.validators import validate_slug





class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    nombre_region = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.nombre_region

    class Meta:
        db_table = "Region"
        verbose_name = "Region"
        verbose_name_plural =  "Regiones"


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nombre_comuna = models.CharField(max_length=30, null=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.nombre_comuna

    class Meta:
        db_table = "Comuna"
        verbose_name = "Comuna"
        verbose_name_plural =  "Comunas"

class Titulo(models.Model):
    nombre_titulo = models.CharField(max_length=40)
    universidad = models.CharField(max_length=40)
    annio_egreso = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre_titulo
    
    class Meta:
        db_table = "Titulo"
        verbose_name = "titulo"
        verbose_name_plural =  "Titulos"


class Convenio(models.Model):
    id_convenio = models.IntegerField(primary_key=True)
    nombre_convenio = models.CharField(max_length=30, null=True)
    descuento = models.IntegerField()

    def __str__(self):
        return self.nombre_convenio
    
    class Meta:
        db_table = "Convenio"
        verbose_name = "Convenio"
        verbose_name_plural =  "Convenios"

class Prevision(models.Model):
    id_prevision = models.IntegerField(primary_key=True)
    nombre_prevision = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.nombre_prevision
    
    class Meta:
        db_table = "Prevision"
        verbose_name = "Prevision"
        verbose_name_plural =  "Previones"


class Especialidad(models.Model):
    id_especialidad = models.IntegerField(primary_key=True)
    nombre_especialidad = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.nombre_especialidad
    
    class Meta:
        db_table = "Especialidad"
        verbose_name = "Especialidad"
        verbose_name_plural =  "Especialidades"


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
        nombre_apellido = self.nombre+" "+self.apellido
        return nombre_apellido

    class Meta:
        db_table = "Especialista"
        verbose_name = "Especialista"
        verbose_name_plural =  "Especialistas"



class Paciente(models.Model):
    rut_paciente = models.CharField(primary_key=True, max_length=15)
    fecha_nacimiento = models.DateField()
    telefono = models.IntegerField()
    sexo = models.CharField(max_length=1, null=True)
    convenio = models.ForeignKey(Convenio, on_delete=models.PROTECT, null=True)
    prevision = models.ForeignKey(Prevision, on_delete=models.PROTECT, null=True)
    usuario =  models.ForeignKey( User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.rut_paciente
    
    class Meta:
        db_table = "Paciente"
        verbose_name = "Paciente"
        verbose_name_plural =  "Pacientes"



class FichaAtencion(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    fecha = models.DateField(null=True) #hay que poner que sea autonow !!!!!
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    motivo_consulta = models.CharField(max_length=500, blank=True, null=True)
    especialista = models.ForeignKey(Especialista, on_delete=models.PROTECT, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return str(self.id_ficha)#self.id_ficha
    
    class Meta:
        db_table = "Ficha_atencion"
        verbose_name = "Ficha atención"
        verbose_name_plural =  "Fichas atención"


horas = [
    [0, "12:00"],
    [1, "13:00"],
    [2, "14:00"],
    [3, "15:00"],
    [4, "16:00"],
    [5, "17:00"],
    [6, "18:00"],
    [7, "19:00"],
    [8, "20:00"]
]

class Estado_cita(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.nombre_estado)

    class Meta:
        db_table = "Estado_Cita"
        verbose_name = "Estado cita"
        verbose_name_plural =  "Estados citas"



estado = [
    [0, "Programada"],
    [1, "Atendido"],
    [2, "Cancelada"],
]

class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    fecha = models.DateField(null=True)
    hora = models.IntegerField(choices=horas, null=True)
    lugar = models.ForeignKey(Region ,on_delete=models.PROTECT, null=True )
    estado = models.ForeignKey(Estado_cita, on_delete=models.PROTECT, null=True)
    slug = models.SlugField(null=False,blank=False, unique=True, validators=[validate_slug])
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='citas')
    especialista = models.ForeignKey(Especialista, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return str(self.id_cita)

    class Meta:
        db_table = "Cita"
        verbose_name = "Cita"
        verbose_name_plural =  "Citas"

def set_slug(sender, instance, *args, **kwargs):
    if instance.slug:
        return
    instance.slug = slugify(instance.fecha.strftime('%d-%m-%Y') + str(instance.hora))

pre_save.connect(set_slug, sender = Cita)


opciones_consulta = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "devolución"]
]

class Consulta(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, null=True)
    correo = models.CharField(max_length=30, null=True)
    telefono = models.IntegerField(null=True)
    opciones_consulta = models.IntegerField(choices=opciones_consulta, null=True)
    mensaje = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.id_consulta
    
    class Meta:
        db_table = "Consulta"
        verbose_name = "Consulta"
        verbose_name_plural =  "Consultas"


class Taller(models.Model):
    id_taller = models.IntegerField(primary_key=True)
    nombre_taller = models.CharField(max_length=50, null=True)
    descripcion = models.CharField(max_length=300, blank=True, null=True)
    imagen = models.ImageField(upload_to="talleres" ,blank=True ,null=True)
    precio = models.IntegerField(blank=True, null=True)
    especialista = models.ForeignKey(Especialista, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.nombre_taller
    
    class Meta:
        db_table = "Taller"
        verbose_name = "Taller"
        verbose_name_plural =  "Talleres"

class Boleta(models.Model): 
    id_boleta = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    monto = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.id_boleta

    class Meta:
        db_table = "Boleta"
        verbose_name = "Boleta"
        verbose_name_plural =  "Boletas"

class Tutor(models.Model):
    rut_tutor = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=50, null=True)
    apellido = models.CharField(max_length=50, null=True)
    correo = models.CharField(max_length=50, null=True)
    telefono = models.IntegerField(null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.rut_tutor
    
    class Meta:
        db_table = "Tutor"
        verbose_name = "Tutor"
        verbose_name_plural =  "Tutores"

