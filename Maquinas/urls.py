from django.urls import path
from . import views
from . import api

urlpatterns = [                     
    path('api/pisos/', api.PisoListApi.as_view(), name='PisoListApi'),
    path('api/camaras/<int:piso_id>/', api.CamaraListApi.as_view(), name='CamaraListApi'),
    path('api/informes/<int:camara_id>/', api.InformeListApi.as_view(), name='InformeListApi'),

    path('api/camaras/actualizar/', api.CamaraUpdateBulkApi.as_view(), name='actualizar_camaras_bulk'),
    
    path('', views.PisoView.as_view(), name='mi_vista'),    
    path('piso/<int:pk>/', views.PisoDetailView.as_view(), name='piso_detail'),  
    path('camara_create/<int:piso>', views.CamaraCreateView.as_view(), name='CamaraCreate'),
    path('camara_update/<int:pk>', views.CamaraUpdateView.as_view(), name='CamaraUpdate'),

    path('informe_create/<int:camara>', views.InformeCreateView.as_view(), name='InformeCreate'),
    
    path('informe_update/<int:pk>', views.InformeUpdateView.as_view(), name='InformeUpdate'),

]