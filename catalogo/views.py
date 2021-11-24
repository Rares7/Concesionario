from django.shortcuts import render

# Create your views here.
from .models import Ciudad, Modelo, BookInstance, Marca
from django.views import generic

class ModelosListView(generic.ListView):
    model = Modelo
    paginate_by = 5
    
class ModelDetailView(generic.DetailView):
    model = Modelo
    template_name = "detalle_coche.html"

    
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


