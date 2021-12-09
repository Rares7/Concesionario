from django.urls import include, path
from catalogo.views import ModelosListView, MarcaDetailView, ModeloCreate, ModeloUpdate, ModeloDelete, SearchResultsListView, \
    crear_modelo
urlpatterns = [
    path('modelos/', ModelosListView.as_view(), name='listado_modelos'),
    path('buscarlibros/', SearchResultsListView.as_view(), name='buscacoches' ),
    path('modelos/crear', crear_modelo, name='crear_coche'),
    path('modelos/modificar/', ModeloUpdate.as_view(), name='modificar_coche'),
    path('modelos/eliminar/', ModeloDelete.as_view(), name='eliminar_coche'),
    path('modelos/<pk>', MarcaDetailView.as_view(), name='marca_detail'),
    
    
   


]