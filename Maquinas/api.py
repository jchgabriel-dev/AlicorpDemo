from rest_framework import generics, status
from .models import Piso, Camara, Informe
from .serializers import PisoSerializer, CamaraSerializer, CamaraUpdateSerializer, InformeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class PisoListApi(generics.ListCreateAPIView):
    queryset = Piso.objects.all() 
    serializer_class = PisoSerializer 


class CamaraListApi(generics.ListCreateAPIView):
    serializer_class = CamaraSerializer
    def get_queryset(self):
        piso_id = self.kwargs.get('piso_id')
        if piso_id:
            return Camara.objects.filter(piso_id=piso_id)
        return Camara.objects.all()
    

class InformeListApi(generics.ListCreateAPIView):
    serializer_class = InformeSerializer
    
    def get_queryset(self):
        camara_id = self.kwargs.get('camara_id')
        if camara_id:
            return Informe.objects.filter(camara_id=camara_id)
        return Informe.objects.all()
    
    
class CamaraUpdateBulkApi(APIView):
    def put(self, request, *args, **kwargs):
        data = request.data

        for camara_data in data:
            
            serializer = CamaraUpdateSerializer(data=camara_data)
            
            if serializer.is_valid():
                camara = Camara.objects.get(id=camara_data['id'])
                camara.latitud = camara_data['latitud']  
                camara.longitud = camara_data['longitud'] 
                camara.save()
            else:
                print("Errores de validación:", serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Cámaras actualizadas correctamente'}, status=status.HTTP_200_OK)
