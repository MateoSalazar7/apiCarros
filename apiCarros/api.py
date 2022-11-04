from .models import Carro
from rest_framework import viewsets, permissions
from .serializers import CarroSerializer

class CarroviewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CarroSerializer
    