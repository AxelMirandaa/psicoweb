import imp
from unicodedata import name
from django.db import router
from django.urls import path, include
from .views import *
from rest_framework import routers 


router = routers.DefaultRouter()
router.register('especialista', EspecialistaViewset)


urlpatterns = [
    path('', home, name="home"),
    path('agregar-especialista/',agregar_especialista,name="agregar_especialista"),
    path('modificar-especialista/<id>/',modificar_especialista, name="modificar_especialista"),
    path('listar-especialistas/', listar_especialistas,name="listar_especialistas"),
    path('eliminar-especialista/<id>/', eliminar_especialista,name="eliminar_especialista"),
    path('citasAgendadas', listaCitas, name="citasAgendadas"),
    path('crearFicha', crearFicha, name="crearFicha"),
    path('especialista', especialista, name="especialista"),
    path('ficha/<id>', ficha, name="ficha"),
    path('listaFichas', listaFichas, name="listaFichas"),
    path('crearCita', crearCita, name="crearCita"),
    path('cita/<id>', cita, name="cita"),
    path('registroPaciente', registroPaciente, name="registroPaciente"),
    path('listaPacientes', listaPacientes, name="listaPacientes"),
    path('listadoEspecialista', listadoEspecialista, name="listadoEspecialista"),
    path('modificarPaciente/<id>', modificarPaciente, name="modificarPaciente"),
    path('eliminarPaciente/<id>', eliminarPaciente, name="eliminarPaciente"),
    path('agendarCita', agendarCita, name="agendarCita"),
    path('modificarCita/<id>', modificarCita, name="modificarCita"),
    path('cancelarCita/<id>', cancelarCita, name="cancelarCita"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),
    path('detalle-especialista/<id>/', detalle_especialista, name="detalle_especialista"),
    path('paypal/',paypal, name='paypal'),
    path('webpay/', carro_webpay, name="carro_webpay"),
	#path('webpay-respuesta/', crearCita, name="carro_webpay_respuesta"),
    path('pasopago/', pasopago, name="pasopago"),


    


]