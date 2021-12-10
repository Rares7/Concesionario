from django.shortcuts import render, redirect

# Create your views here.
from .models import Ciudad, Modelo, BookInstance, Marca
from django.views import generic
from django.views.generic import ListView
from catalogo.forms import ModeloForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required

class ModelosListView(generic.ListView):
    model = Modelo
    paginate_by = 5
    
class MarcaDetailView(generic.DetailView):
    model = Modelo

class SearchResultsListView(ListView):
    model = Modelo
    context_object_name = 'modelos'
    template_name = 'search_results.html'  # No usará la plantilla estándar del ListView
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        if query:
            return Modelo.objects.filter(title__icontains=query)
        return []  # cuando entramos a buscar o si no se introduc

@login_required
def crear_modelo(request):
    if request.method == 'POST':
        form = ModeloForm(request.POST)
        if form.is_valid():
            form.save()
            # Mensaje para informar éxito redirección
            messages.add_message(request, 
                messages.SUCCESS, 
                'Modelo creado.')
            return redirect('/')
    else:
        form = ModeloForm()
    datos = {'form': ModeloForm()}
    return render(request, 'modelo_form.html', 
        context=datos)
        
class ModeloCreate(SuccessMessageMixin, CreateView):
    model = Modelo
    #fields = '__all__'
    template_name = 'modelo_form.html'
    success_url = '/'
    form_class = ModeloForm
    success_message = "%(nombre)s %(modelo)s se ha creado correctamente"


class ModeloUpdate(SuccessMessageMixin, generic.UpdateView):
    model = Modelo
    fields = '__all__'
    template_name = 'modificar_coche.html'
    success_url = '/'
    success_message = "%(nombre)s %(modelo)s se ha modificado correctamente"
    paginate_by = 5


class ModeloDelete(generic.DeleteView):
    model = Modelo
    success_url = '/catalago/modelos' #reverse('listado_autores')
    success_message = "El modelo se ha borrado correctamente"
    template_name = 'coche_confirmar_borrado.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ModeloDelete, self).delete(
            request, *args, **kwargs)
    
    paginate_by = 5

    
def indice(request):
    """
    Función vista para la página inicio del sitio.
    """
    datos = {'coche': 'Marca'}
    modelos = Modelo.objects.all().order_by('-id')[:5]
    datos['modelos'] = modelos

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context=datos)


