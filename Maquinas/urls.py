from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.PisoView.as_view(), name='mi_vista'),
    path('pisos/<int:pk>/', views.PisoDetailView.as_view(), name='piso_detail'),
    
    path('api/pisos/', api.PisoListApi.as_view(), name='PisoListApi'),
]