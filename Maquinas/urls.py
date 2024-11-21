from django.urls import path
from . import views

urlpatterns = [
    path('', views.MapaView.as_view(), name='mi_vista'),
    path('guardar_ubicaciones/', views.guardar_ubicaciones, name='guardar_ubicaciones'),

]