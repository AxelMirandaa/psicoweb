from dataclasses import field
import imp
from django import forms
from .models import Especialista



class especialistaForm(forms.ModelForm):
    
    class Meta:
        model = Especialista
        fields = '__all__'
