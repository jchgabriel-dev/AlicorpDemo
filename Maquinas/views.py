from django.shortcuts import render

from django.views.generic import TemplateView
from .models import Plano, Marcador
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


class MapaView(TemplateView):
    template_name = 'Mapa.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plano = Plano.objects.first() 
        objetos = Marcador.objects.all()
        
        context['PLANO'] = plano 
        context['MARCADORES'] = objetos

        marcadores = [
            {
                'id': obj.id,
                'nombre': obj.nombre,
                'latitud': obj.latitud,
                'longitud': obj.longitud,
            }
            for obj in objetos
        ]

        context['PUNTOS'] = json.dumps(marcadores)


        return context



def guardar_ubicaciones(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        for item in data:
            marcador = Marcador.objects.get(id=item['id'])
            marcador.latitud = item['lat']
            marcador.longitud = item['lon']
            marcador.save() 
        return JsonResponse({'status': 'success', 'message': 'Ubicaciones guardadas correctamente'})
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)