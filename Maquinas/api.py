from rest_framework import generics
from .models import Piso
from .serializers import PisoSerializer

class PisoListApi(generics.ListCreateAPIView):
    queryset = Piso.objects.all() 
    serializer_class = PisoSerializer 


