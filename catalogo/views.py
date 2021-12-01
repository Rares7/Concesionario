from django.shortcuts import render

# Create your views here.
from .models import Ciudad, Modelo, BookInstance, Marca
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ModelosListView(generic.ListView):
    model = Modelo
    paginate_by = 5
    
class MarcaDetailView(generic.DetailView):
    model = Marca

class AuthorCreate(CreateView):
    model = Modelo
    fields = '__all__'

class AuthorUpdate(UpdateView):
    model = Modelo
    fields = '_all__'

class AuthorDelete(DeleteView):
    model = Modelo
    success_url = reverse_lazy('modelos')

    
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


