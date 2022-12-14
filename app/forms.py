from dataclasses import field
import imp
from django import forms
from .models import Especialista, FichaAtencion, Cita, Paciente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import date
from datetime import timedelta 

from django.utils.timezone import now


class DateInput2(forms.DateInput):
    input_type = 'date'

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


#Formulario para la cración de especialistas
class especialistaForm(forms.ModelForm):
     
    class Meta:
        model = Especialista
        #fields = '__all__'
        fields = ['rut_especialista','nombre','apellido','correo','telefono','precio_consulta','descripcion','imagen','region','especialidad','tipo_titulo']


#Formalario para la creación de fichas
class fichaForm(forms.ModelForm):
    
    class Meta:
        model = FichaAtencion
        fields = '__all__'
        widgets = {
            'fecha': DateInput(),
        }     


#Formulario para el registro de usuarios
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        
    

#Formulario para el registro de las citas medicas
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
            cita = Cita.objects.get(hora = self.cleaned_data["hora"], fecha = self.cleaned_data["fecha"], especialista = self.cleaned_data["especialista"])
        
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
        #fields = '__all__'
        fields = ['rut_paciente','fecha_nacimiento','telefono','genero','genero','prevision']

        widgets = {
            'fecha_nacimiento': DateInput2(),
        }         

class pacienteModificaForm(forms.ModelForm):
    
    class Meta:
        model = Paciente
        fields = ['rut_paciente','fecha_nacimiento','telefono','genero','genero','prevision']
        widgets = {
            'fecha_nacimiento': DateInput2(),
        }    

            