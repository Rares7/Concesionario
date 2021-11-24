from django.urls import include, path
from catalogo.views import ModelosListView 

urlpatterns = [
    path('modelos/', ModelosListView.as_view(), 
        name='listado_modelos'),

]