import imp
from django.urls import path
from .views import home, agregar_especialista

urlpatterns = [
    path('', home, name="home"),
    path('agregar-especialista',agregar_especialista,name="agregar_especialista")
]