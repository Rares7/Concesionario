from django.shortcuts import render

# Create your views here.
from .models import Ciudad, Modelo, BookInstance, Marca

def indice(request):
    """
    Función vista para la página inicio del sitio.
    """
    datos = {'autor': 'Marca'}
    modelos = Modelo.objects.all().order_by('-id')[:5]

    datos['modelos'] = modelos

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context=datos)