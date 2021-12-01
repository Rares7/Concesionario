from django.forms import ModelForm, DateInput
from catalogo.models import Modelo
from django import forms


class ModeloForm(ModelForm):
    '''Formulario para crear coches'''
    class Meta:
        model = Modelo
        fields = '__all__'
        widgets = {
            'Fecha en la que se añadio': DateInput(attrs={'type': 'date'}),
        }

