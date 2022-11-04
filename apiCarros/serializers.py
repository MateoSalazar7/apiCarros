from rest_framework import serializers
from .models import Carro

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ('id', 'marca', 'modelo','año','color','tipo_combustible','descripcion','puertas','transmision','motor','tipo_carroceria')
        read_only_fields = ('modelo',)
