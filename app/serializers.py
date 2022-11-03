from imp import source_from_cache
from pyexpat import model
#from attr import field
from .models import Especialista
from rest_framework import serializers

class EspecialistaSerializer(serializers.ModelSerializer):
    #nombre_region = serializers.CharField(read_only=True, source="region.nombre_region")
    #nombre_especialidad = serializers.CharField(read_only=True, source="especialidad.nombre_especialidad")
    #nombre_titulo = serializers.CharField(read_only=True, source="tipo_titulo.nombre_titulo")
    class Meta:
        model = Especialista
        fields = '__all__'