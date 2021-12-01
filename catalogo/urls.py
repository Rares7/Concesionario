from django.urls import include, path
from catalogo.views import ModelosListView, MarcaDetailView, crear_coche
urlpatterns = [
    path('modelos/', ModelosListView.as_view(), 
        name='listado_modelos'),
    path('modelos/<pk>', MarcaDetailView.as_view(), 
        name='marca_detail'),
    path('autor/crear', crear_coche, name='crear_coche'),

]