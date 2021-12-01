from django.forms import ModelForm, DateInput
from catalogo.models import Modelo
from django import forms


class MarcaForm(ModelForm):
    '''Formulario para crear autores'''
    class Meta:
        model = Modelo
        fields = '__all__'
        widgets = {
            'Fecha en la que se añade': DateInput(attrs={'type': 'date'}),
        }
    

