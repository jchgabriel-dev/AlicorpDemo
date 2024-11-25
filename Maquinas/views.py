from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, CreateView, UpdateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . models import Piso, Camara, Informe
from PIL import Image
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .forms import CamaraForm, InformeForm
from .serializers import CamaraSerializer

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
        
        context['CAMARA_URL'] = reverse('CamaraCreate', args=[self.object.id]) 
        context['MARCADORES'] = Camara.objects.filter(piso=self.object.id)
        
        camaras = Camara.objects.filter(piso=piso)
        camaras_serializer = CamaraSerializer(camaras, many=True)
        context['PUNTOS'] = json.dumps(camaras_serializer.data)

        return context
    
    
class CamaraCreateView(CreateView):
    template_name = 'camara.html'
    model = Camara
    form_class = CamaraForm
    
    def get_success_url(self):
        piso_id = self.kwargs.get('piso')  
        if piso_id:
            return reverse('piso_detail', args=[piso_id]) 
        return reverse('mi_vista')
    
    def get_initial(self):      
        initial = super().get_initial()
        piso_id = self.kwargs.get('piso')            
        
        if piso_id:
            print(piso_id)
            piso = get_object_or_404(Piso, pk=piso_id)
            initial['piso'] = piso
        
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        

        piso_id = self.kwargs.get('piso') 
        if piso_id:                           
            context['RETURN_URL'] = reverse('piso_detail', args=[piso_id]) 

        return context
    

class CamaraUpdateView(UpdateView):
    template_name = 'Camara.html'
    model = Camara
    form_class = CamaraForm
    
    def get_success_url(self):
        camara = self.get_object()        
        if camara and camara.piso:
            return reverse('piso_detail', args=[camara.piso.id])  
        
        return reverse('mi_vista')    
    
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        camara = self.get_object()
        if camara and camara.piso:
            context['RETURN_URL'] = reverse('piso_detail', args=[camara.piso.id])

        return context
    
    

class InformeCreateView(CreateView):
    template_name = 'Informe.html'
    model = Informe
    form_class = InformeForm
    
    def get_success_url(self):
        camara_id = self.kwargs.get('camara')  
    
        if camara_id:
            camara = get_object_or_404(Camara, pk=camara_id)
            return reverse('piso_detail', args=[camara.piso.id])  
        
        return reverse('mi_vista')

    def get_initial(self):      
        initial = super().get_initial()
        camara_id = self.kwargs.get('camara')            
        
        if camara_id:
            camara = get_object_or_404(Camara, pk=camara_id)
            initial['camara'] = camara
        
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        

        camara_id = self.kwargs.get('camara')  
        if camara_id:             
            camara = get_object_or_404(Camara, pk=camara_id)                          
            context['RETURN_URL'] = reverse('piso_detail', args=[camara.piso.id]) 

        return context
    
    
class InformeUpdateView(UpdateView):
    template_name = 'Informe.html'
    model = Informe
    form_class = InformeForm
    
    def get_success_url(self):
        informe = self.get_object()
        
        if informe and informe.camara and informe.camara.piso:
            return reverse('piso_detail', args=[informe.camara.piso.id])  
        
        return reverse('mi_vista')    
    
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        informe = self.get_object()

        if informe and informe.camara and informe.camara.piso:
            context['RETURN_URL'] = reverse('piso_detail', args=[informe.camara.piso.id])

        return context