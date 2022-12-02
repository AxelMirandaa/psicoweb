from dataclasses import field
import imp
from django import forms
from .models import Especialista, FichaAtencion, Cita, Paciente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import date
from datetime import timedelta 

from django.utils.timezone import now




  
        


#datepicker widgets
class DateInput(forms.DateInput):
    input_type = 'date'
    
    def get_context(self, name, value, attrs):
        today = date.today()  
        proximoannio = today + timedelta(weeks = 53) 
        attrs.setdefault('min', today)
        attrs.setdefault('max', proximoannio)
        return super().get_context(name, value, attrs)


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
        #Cita.objects.exclude(fecha=datetime.now())
        widgets = {
            'fecha': DateInput(),
        }       
    
    def clean(self):
        try:
            cita = Cita.objects.get(hora = self.cleaned_data["hora"], fecha = self.cleaned_data["fecha"])
        
            if not self.instance.pk:
                raise forms.ValidationError("hora ya tomada")
            elif self.instance.pk!=cita.pk:
                raise forms.ValidationError("cambio no permitido, hora ya tomada")
        except Cita.DoesNotExist:
            pass
        return self.cleaned_data
          
        
class pacienteForm(forms.ModelForm):
    
    class Meta:
        model = Paciente
        fields = '__all__'       
            