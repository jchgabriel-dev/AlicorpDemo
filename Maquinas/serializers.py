from rest_framework import serializers
from .models import Piso, Camara, Informe

class PisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piso
        fields = '__all__' 
        
class CamaraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camara
        fields = '__all__'

class InformeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informe
        fields = '__all__'
        
 
class CamaraUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    latitud = serializers.FloatField()
    longitud = serializers.FloatField()