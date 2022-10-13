from ast import If
from django.shortcuts import render
from django.urls import is_valid_path
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