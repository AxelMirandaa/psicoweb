import imp
from unicodedata import name
from django.db import router
from django.urls import path, include
from .views import home, agregar_especialista, modificar_especialista, listar_especialistas,\
    eliminar_especialista, citasAgendadas, crearFicha, especialista, ficha, infoPacientes, \
    registro, EspecialistaViewset, detalle_especialista, paypal
from rest_framework import routers 


router = routers.DefaultRouter()
router.register('especialista', EspecialistaViewset)


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
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),
    path('detalle-especialista/<id>/', detalle_especialista, name="detalle_especialista"),
    path('paypal/',paypal, name='paypal'),

    


]