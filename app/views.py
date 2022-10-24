from ast import If
from django.forms import PasswordInput
from django.shortcuts import render, redirect, get_object_or_404 
from django.urls import is_valid_path
from requests import request
from .models import Especialista, FichaAtencion
from .forms import especialistaForm, fichaForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.

def home(request):
    especialistas = Especialista.objects.all()
    data = {
        'especialistas':especialistas
    }

    return render(request, 'app/home.html', data)


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



def listar_especialistas(request):
    especialistas = Especialista.objects.all()
    data = {
        'especialistas': especialistas

    }
    
    return render(request, 'app\especialistas_lista\listar.html', data)




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