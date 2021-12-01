from django.urls import include, path
from catalogo.views import ModelosListView, MarcaDetailView, ModeloCreate, ModeloUpdate, ModeloDelete
urlpatterns = [
    path('modelos/', ModelosListView.as_view(), 
        name='listado_modelos'),
    path('modelos/<pk>', MarcaDetailView.as_view(), 
        name='marca_detail'),
    path('modelos/crear/<int:pk>', ModeloCreate.as_view(), name='crear_coche'),
    path('modelos/modificar/<int:pk>', ModeloUpdate.as_view(), name='modificar_coche'),
    path('modelos/eliminar/<int:pk>', ModeloDelete.as_view(), name='coche_confirmar_borrado'),


]