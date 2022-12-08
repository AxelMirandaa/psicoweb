import imp
from django.contrib import admin
from .models import *
from utilidades import formularios


class CitaAdmin(admin.ModelAdmin):
	list_display = ('id_cita','fecha','hora','lugar','usuario','especialista')
	search_fields = ('id_cita','fecha','hora','lugar','usuario','especialista')
	exclude = ('slug',) 

class EspecialistaAdmin(admin.ModelAdmin):
	list_display = ('rut_especialista','nombre','apellido','correo','telefono','precio_consulta','especialidad')
	search_fields = ('rut_especialista','nombre','apellido','correo','telefono','precio_consulta','especialidad')

class TrackingAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'fecha')
    search_fields = ('id', 'descripcion')



admin.site.register(Tracking,TrackingAdmin)
admin.site.register(Estado)
admin.site.register(Carrito)
admin.site.register(OrdenDeCompra)
admin.site.register(Genero)
admin.site.register(Cita, CitaAdmin)
admin.site.register(Comuna)
admin.site.register(Consulta)
admin.site.register(Especialidad)
admin.site.register(Especialista, EspecialistaAdmin)
admin.site.register(FichaAtencion)
admin.site.register(Paciente)
admin.site.register(Prevision)
admin.site.register(Region)
admin.site.register(Taller)
admin.site.register(Titulo)
admin.site.register(Estado_cita)

admin.site.site_header = 'Clínica Locura'
admin.site.index_title = 'Clínica Locura'
admin.site.site_title = 'Clínica Locura'



