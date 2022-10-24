import imp
from unicodedata import name
from django.urls import path
from .views import home, agregar_especialista, modificar_especialista, listar_especialistas,\
    eliminar_especialista, citasAgendadas, crearFicha, especialista, ficha, infoPacientes, registro

urlpatterns = [
    path('', home, name="home"),
    path('agregar-especialista/',agregar_especialista,name="agregar_especialista"),
    path('modificar-especialista/<id>/',modificar_especialista, name="modificar_especialista"),
    path('listar-especialistas/', listar_especialistas,name="listar_especialistas"),
    path('eliminar-especialista/<id>/', eliminar_especialista,name="eliminar_especialista"),
    path('citasAgendadas', citasAgendadas, name="citasAgendadas"),
    path('crearFicha', crearFicha, name="crearFicha"),
    path('especialista', especialista, name="especialista"),
    path('ficha', ficha, name="ficha"),
    path('infoPacientes', infoPacientes, name="infoPacientes"),
    path('registro/', registro, name="registro")


]