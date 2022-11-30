from dataclasses import field
import imp
from django import forms
from .models import Especialista, FichaAtencion, Cita, Paciente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#datepicker widgets
class DateInput(forms.DateInput):
    input_type = 'date'

# widget para fecha y hora
class TimePickerInput(forms.TimeInput):
        input_type = 'time'

#widgets para horas

class DateTimePickerInput(forms.DateTimeInput):
        input_type = 'datetime'

class especialistaForm(forms.ModelForm):
     
    class Meta:
        model = Especialista
        fields = '__all__'


class fichaForm(forms.ModelForm):
    
    class Meta:
        model = FichaAtencion
        fields = '__all__'
        widgets = {
            'fecha': DateInput(),
        }     


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
    
class citaForm(forms.ModelForm):
    
    class Meta:
        model = Cita
        fields = ['fecha','hora','lugar','especialista']
        widgets = {
            'fecha': DateInput(),
        }       
        
class pacienteForm(forms.ModelForm):
    
    class Meta:
        model = Paciente
        fields = '__all__'       
            