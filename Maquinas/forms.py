from django import forms
from datetime import date, datetime, time
from .models import Camara, Informe

class NoLabelModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NoLabelModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                field.widget.attrs['type'] = 'date'
                field.widget.format = '%Y-%m-%d'

            if isinstance(field, forms.TimeField):
                field.widget.attrs['type'] = 'time'
                field.widget.format = '%H:%M'
            field.label = False
            
class BaseForm(NoLabelModelForm):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), initial=date.today)


class CamaraForm(BaseForm):
    class Meta:
        model = Camara
        fields = '__all__' 
    
    

class InformeForm(BaseForm):
    class Meta:
        model = Informe
        fields = '__all__' 