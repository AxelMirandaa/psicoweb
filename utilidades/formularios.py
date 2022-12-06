from app.models import *
from datetime import date
from django.utils.html import format_html

def getFechaActual():
	return date.today()

def get_perfiles_choices():
    return [
        (valve.pk, valve.nombre) for valve in Paciente.objects.all()
    ]




def get_estados_choices():
    return [
        (valve.pk, valve.nombre) for valve in Estado.objects.filter(id__in=[1, 2]).all()
    ]



def get_generos_choices():
    return [
        (valve.pk, valve.nombre) for valve in Genero.objects.all()
    ]



############HELPERS MODELOS

def set_estado(obj):
    return obj.estado.nombre
set_estado.short_description = 'Estado'

def set_genero(obj):
    return obj.genero.nombre
set_genero.short_description = 'Género'



def set_perfiles(obj):
    return obj.perfiles.nombre
set_perfiles.short_description = 'Perfil'

def set_user(obj):
    return f"{obj.user.first_name} {obj.user.last_name}"
set_user.short_description = 'Usuario'


def set_users_metadata(obj):
    return f"{obj.users_metadata.user.first_name} {obj.users_metadata.user.last_name}"
set_users_metadata.short_description = 'Usuario'


def set_producto_categoria(obj):
    return obj.producto_categoria.nombre
set_producto_categoria.short_description = 'Categoría'


def set_producto(obj):
    return obj.producto.nombre
set_producto.short_description = 'Producto'


def set_correo(obj):
    return obj.user.username
set_correo.short_description = 'E-Mail'


def get_descripcion(obj):
    return format_html(f"""<div style="word-wrap: break-word;width:200px;">{obj.descripcion[0:100]}......</div>""")
get_descripcion.short_description = 'Descripción'


