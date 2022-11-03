from dataclasses import field
import imp
from django import forms
from .models import Especialista, FichaAtencion, Cita, Paciente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class especialistaForm(forms.ModelForm):
     
    class Meta:
        model = Especialista
        fields = '__all__'


class fichaForm(forms.ModelForm):
    
    class Meta:
        model = FichaAtencion
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
class citaForm(forms.ModelForm):
    
    class Meta:
        model = Cita
        fields = '__all__'       
        
class pacienteForm(forms.ModelForm):
    
    class Meta:
        model = Paciente
        fields = '__all__'       
            