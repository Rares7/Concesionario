from django.urls import include, path
from catalogo.views import ModelosListView, MarcaDetailView, ModeloCreate, ModeloUpdate, ModeloDelete
urlpatterns = [
    path('modelos/', ModelosListView.as_view(), name='listado_modelos'),
    path('modelos/crear', ModeloCreate.as_view(), name='crear_coche'),
    path('modelos/modificar', ModeloUpdate.as_view(), name='modificar_coche'),
    path('modelos/eliminar', ModeloDelete.as_view(), name='coche_confirmar_borrado'),
    path('modelos/<pk>', MarcaDetailView.as_view(), name='marca_detail'),
    
    
   


]