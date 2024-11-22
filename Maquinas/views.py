from django.shortcuts import render

from django.views.generic import TemplateView, DetailView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . models import Piso
from PIL import Image


class PisoView(TemplateView):
    template_name = "Piso.html"


class PisoDetailView(DetailView):
    model = Piso
    template_name = 'mapa.html' 
    context_object_name = 'piso'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        piso = self.object
        
        if piso.imagen:
            with Image.open(piso.imagen.path) as img:
                context['image_width'], context['image_height'] = img.size
        else:
            context['image_width'], context['image_height'] = 500, 500

        return context