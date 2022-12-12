from ast import If
from django.forms import PasswordInput
from django.shortcuts import render, redirect, get_object_or_404 
from django.http import Http404, HttpResponseRedirect, HttpResponse
from utilidades import utilidades#, webpay
from django.urls import is_valid_path
from requests import request
from .models import *
from .forms import especialistaForm, fichaForm, CustomUserCreationForm, citaForm, pacienteForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import EspecialistaSerializer
import json
from django.conf import settings
from django.contrib.auth.hashers import make_password
import random
import requests



# Create your views here.

class EspecialistaViewset(viewsets.ModelViewSet):
    queryset = Especialista.objects.all()
    serializer_class = EspecialistaSerializer


def paypal(request):

    especialistas = Especialista.objects.all()
    data = {
        'especialistas':especialistas
    }
    
    return render(request, 'app/paypal.html',data)





def detalle_especialista(request,id):

   ## especialista = get_object_or_404(Especialista, rut_especialista=id)

    try:
        datos = Especialista.objects.filter(id_especialista=id).get()
    except Especialista.DoesNotExist:
        pass

  #  data = {
   #     'form': especialistaForm(instance=especialista)
   # }
    return render(request, 'app/detalleEspecialista.html',{'datos':datos})

def home(request):
    especialistas = Especialista.objects.all()
    talleres = Taller.objects.all()
    data = {
        'especialistas':especialistas,
        'talleres': talleres
    }

    return render(request, 'app/home.html', data)

@permission_required('app.add_especialista')
def agregar_especialista(request):
#
    data = {
        'form':especialistaForm()
    }

    if request.method == 'POST':
        formulario = especialistaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            
            usuario = User.objects.create(username=formulario.cleaned_data["correo"], 
                                    first_name = formulario.cleaned_data["nombre"],
                                    last_name = formulario.cleaned_data["apellido"],
                                    email = formulario.cleaned_data["correo"],
                                    password = make_password('clinicalocura'),
                                    is_staff = 1)
                                    
            formulario.usuario = usuario
            #usuario.groups.add = 'user_especialista'
            
            
            messages.success(request, "Guardado correctamente")
        else:
            data["form"] = formulario

    return render(request, 'app/especialistas_lista/agregar.html', data)


@permission_required('app.view_especialista')
def listar_especialistas(request):
    especialistas = Especialista.objects.all()
    data = {
        'especialistas': especialistas

    }
    
    return render(request, 'app\especialistas_lista\listar.html', data)



@permission_required('app.change_especialista')
def modificar_especialista(request, id):
    
    especialista = get_object_or_404(Especialista, id_especialista=id)

    data = {
        'form': especialistaForm(instance=especialista)
    }

    if request.method == 'POST':
        formulario = especialistaForm(data=request.POST, instance=especialista ,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_especialistas")
        
        data['form'] = formulario

    return render(request,'app/especialistas_lista/modificar.html',data)


@permission_required('app.delete_especialista')
def eliminar_especialista(request, id):
    especialista = get_object_or_404(Especialista, id_especialista=id)
    especialista.delete()
    messages.success(request, "Eliminado correctamente")

    return redirect(to="listar_especialistas")

def crearFicha(request):
    
    data = {
        'form':fichaForm()
    }

    if request.method == 'POST':
        formulario = fichaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Ficha creada correctamente")
        else:
            data["form"] = formulario
    
    return render(request, 'app/crearFicha.html', data)

def especialista(request):
    citas = Cita.objects.all()
    data = {
        'citas' : citas
    }
    return render(request, 'app/especialista.html', data)



def ficha(request, id):
    ficha = FichaAtencion.objects.get(id_ficha=id)
    data = {
        'form':fichaForm(instance=ficha)
    }

    if request.method == 'POST':
        formulario = fichaForm(data=request.POST, instance=ficha)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado correctamente")
    #    else:
    #        data["form"] = formulario
    return render(request, 'app/ficha.html', data)

def listaFichas(request):
    ficha = FichaAtencion.objects.all()
    data = {
        'ficha' : ficha
    }
    
    return render(request, 'app/listaFichas.html', data)
 
 #Mustra las citas del usuasrio logeado
@login_required
def listaCitas(request):
    usuario = request.user
    citas = usuario.citas.all()
    #citas = Cita.objects.all()
    data = {
        'citas' : citas
    }
    
    return render(request, 'app/citasAgendadas.html', data)

def cita(request, id):
    cita = Cita.objects.get(id_cita=id)
    data = {
        'form':citaForm(instance=cita)
    }
    if request.method == 'POST':
        formulario = citaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cita Modificada correctamente")
        else:
            data["form"] = formulario
    
    return render(request, 'app/cita.html', data)


#Crea una cita con el usuario logeado 
@login_required
def crearCita(request):
    
    user = get_object_or_404 (User, pk=request.user.pk)
    estadoCita = get_object_or_404(Estado_cita, pk = 1)
    valida_hora = Cita.objects.all()


    data = {
        'form':citaForm()
    }

    if request.method == 'POST':
        formulario = citaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            cita = formulario.save(commit=False)
            cita.usuario = user
            cita.estado = estadoCita

            cita.save()
            messages.success(request, "Cita creada correctamente")
            return redirect(to="pasopago")
        else:
            data["form"] = formulario
    
    return render(request, 'app/crearCita.html', data)







def registroPaciente(request):
    
    data = {
        'form': pacienteForm()
        
    }

    if request.method == 'POST':
        formulario = pacienteForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            messages.success(request, "Agregado correctamente")

            formulario.save()
            messages.success(request, "Agregado correctamente")
        else:
            data["form"] = formulario
    
    return render(request, 'app/registroPaciente.html', data)

def listaPacientes(request):
    paciente = Paciente.objects.all()
    data = {
        'paciente' : paciente
    }
    
    return render(request, 'app/listaPacientes.html', data)

def listadoEspecialista(request):
    especialistas = Especialista.objects.all()
    data = {
        'especialistas': especialistas

    }

    
    return render(request, 'app/listadoEspecialista.html', data)






def modificarPaciente(request, id):
    paciente = Paciente.objects.get(id_paciente=id)
    data = {
        'form': pacienteForm(instance=paciente)
    }

    if request.method == 'POST':
        formulario = pacienteForm(data=request.POST, instance=paciente)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="home")
    
        data["form"] = formulario
    return render(request, 'app/modificarPaciente.html', data)

def eliminarPaciente(request, id):
    paciente = get_object_or_404(Paciente, rut_paciente=id)
    paciente.delete()
    messages.success(request, "Eliminado correctamente")

    return redirect(to="listaPacientes")


@login_required
def agendarCita(request):
    
    data = {
        'form':citaForm()
    }

    if request.method == 'POST':
        formulario = citaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Ficha creada correctamente")
        else:
            data["form"] = formulario
    
    
    return render(request, 'app/agendarCita.html', data)


def modificarCita(request, id):
    
    cita = get_object_or_404(Cita, id_cita=id)

    data = {
        'form': citaForm(instance=cita)
    }

    if request.method == 'POST':
        formulario = citaForm(data=request.POST, instance=cita ,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="citasAgendadas")
        
        data['form'] = formulario

    return render(request,'app/modificarCita.html',data)



def cancelarCita(request,id):
    cita = Cita.objects.get(id_cita=id)
    cita.delete()
    return redirect(to="citasAgendadas")




#REGISTRO DE USUARIOS
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            Paciente.objects.create(id_paciente=user.id, usuario = user)
            #UsersMetadata.objects.create(correo='', telefono='', direccion='', user_id=user.id)
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return  redirect(to="../modificarPaciente/"+str(user.id))

    return render(request, 'registration/registro.html', data)




#pago webpay

def crearTransaccion():
	#se crea la orden de compra
	suma=20000
	

	buy_order = (random.randrange(1000000, 99999999))
	session_id = str(random.randrange(1000000, 99999999))
	amount = suma
	ruta=f"http://127.0.0.1:8000/"
	endpoint=settings.WEBPAY_URL
	payload={
		 "buy_order": buy_order,
		 "session_id": session_id,
		 "amount": amount,
		 "return_url": ruta
		}
	cabeceros = {'content-type': 'application/json', 'Tbk-Api-Key-Id': settings.WEBPAY_ID, 'Tbk-Api-Key-Secret': settings.WEBPAY_SECRET}
	response= requests.post(endpoint, json=payload, headers=cabeceros)
	#response.status_code
	respuesta=json.loads(response.text)
	#guardo el token recibido
	#retorno token y URL
	ruta=f"{respuesta['url']}{respuesta['token']}"
	return respuesta



def carro_webpay(request):
   # sesion=f"{request.POST['especialista']}"
    result=crearTransaccion()
    return render(request, 'app/webpay.html', {'url': result['url'], 'token': result['token']})





def pasopago(request):

    return render(request, 'app/pasopago.html')
