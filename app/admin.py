import imp
from django.contrib import admin
from .models import Boleta,Cita,Comuna,Consultas,Convenio,Especialidad,Especialista,FichaAtencion,Paciente,Prevision,Region,Taller,TipoTitulo,Tutor


# Register your models here.


admin.site.register(Boleta)
admin.site.register(Cita)
admin.site.register(Comuna)
admin.site.register(Consultas)
admin.site.register(Convenio)
admin.site.register(Especialidad)
admin.site.register(Especialista)
admin.site.register(FichaAtencion)
admin.site.register(Paciente)
admin.site.register(Prevision)
admin.site.register(Region)
admin.site.register(Taller)
admin.site.register(TipoTitulo)
admin.site.register(Tutor)


