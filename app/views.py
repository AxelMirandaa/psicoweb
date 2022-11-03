from ast import If
from django.forms import PasswordInput
from django.shortcuts import render, redirect, get_object_or_404 
from django.urls import is_valid_path
from requests import request
from .models import Especialista, FichaAtencion
from .forms import especialistaForm, fichaForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import EspecialistaSerializer


# Create your views here.

class EspecialistaViewset(viewsets.ModelViewSet):
    queryset = Especialista.objects.all()
    serializer_class = EspecialistaSerializer


def paypal(request):
    return render(request, 'app/paypal.html')


def detalle_especialista(request,id):

   ## especialista = get_object_or_404(Especialista, rut_especialista=id)

    try:
        datos = Especialista.objects.filter(rut_especialista=id).get()
    except Especialista.DoesNotExist:
        pass

  #  data = {
   #     'form': especialistaForm(instance=especialista)
   # }
    return render(request, 'app/detalleEspecialista.html',{'datos':datos})

def home(request):
    especialistas = Especialista.objects.all()
    data = {
        'especialistas':especialistas
    }

    return render(request, 'app/home.html', data)

@permission_required('app.add_especialista')
def agregar_especialista(request):

    data = {
        'form':especialistaForm()
    }

    if request.method == 'POST':
        formulario = especialistaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
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
    
    especialista = get_object_or_404(Especialista, rut_especialista=id)

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
    especialista = get_object_or_404(Especialista, rut_especialista=id)
    especialista.delete()
    messages.success(request, "Eliminado correctamente")

    return redirect(to="listar_especialistas")


def citasAgendadas(request):
    
    return render(request, 'app/citasAgendadas.html')

def crearFicha(request):
    
    data = {
        'form':fichaForm()
    }

    if request.method == 'POST':
        formulario = fichaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
    
    return render(request, 'app/crearFicha.html', data)

def especialista(request):
    
    return render(request, 'app/especialista.html')

def ficha(request, id):
    ficha = FichaAtencion.objects.get(id_ficha=id)
    data = {
        'form' : fichaForm(instance=ficha)
    }
    
    return render(request, 'app/ficha.html', data)

def infoPacientes(request):
    
    return render(request, 'app/infoPacientes.html')



def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te haz registrado correctamente")
            return  redirect(to="home")

    return render(request, 'registration/registro.html', data)