from ast import If
from django.shortcuts import render, redirect, get_object_or_404 
from django.urls import is_valid_path
from requests import request
from .models import Especialista
from .forms import especialistaForm


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
            data["mensaje"] = "guardado correctamente"
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
            return redirect(to="listar_especialistas")
        
        data['form'] = formulario

    return render(request,'app/especialistas_lista/modificar.html',data)



def eliminar_especialista(request, id):
    especialista = get_object_or_404(Especialista, rut_especialista=id)
    especialista.delete()
    return redirect(to="listar_especialistas")


