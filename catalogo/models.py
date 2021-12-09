from django.db import models
from django.db.models.base import Model

# Create your models here.
class Ciudad(models.Model):
    """
    Modelo que representa un género literario (p. ej. ciencia ficción, poesía, etc.).
    """
    name = models.CharField(max_length=200, help_text="Ingrese la ciudad en la que se encuentra el coche")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.name
    
    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Modelo(models.Model):
    """
    Modelo que representa un modelo de coche.
    """

    modelo = models.CharField('Titulo', max_length=200)

    marca = models.ForeignKey('marca', on_delete=models.SET_NULL, null=True)
    # ForeignKey, ya que un libro tiene un solo autor, pero el mismo autor puede haber escrito muchos libros.
    # 'Author' es un string, en vez de un objeto, porque la clase Author aún no ha sido declarada.

    precio = models.CharField(max_length=1000, help_text="Ingrese el precio del coche")

    ciudad = models.ManyToManyField(Ciudad, help_text="Seleccione una ciudad para este coche")
    # ManyToManyField, porque un género puede contener muchos libros y un libro puede cubrir varios géneros.
    # La clase Genre ya ha sido definida, entonces podemos especificar el objeto arriba.

    def __str__(self):
        """
        String que representa al objeto Book
        """
        return self.modelo

    def muestra_ciudad(self):
        '''Muestra ciudad para admin'''
        return ', '.join([gen.name for gen in self.Ciudad.all()[:2]]) 
    muestra_ciudad.short_description = 'Ciudad'


import uuid # Requerida para las instancias de libros únicos

class BookInstance(models.Model):
    """
    Modelo que representa una copia específica de un coche (i.e. que puede ser prestado por la biblioteca).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este coche particular en toda la biblioteca")
    modelo = models.ForeignKey('Modelo', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del coche')

    class Meta:
        ordering = ["due_back"]


    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s (%s)' % (self.id,self.modelo.modelo)

class Marca(models.Model):
    """
    Modelo que representa un autor
    """
    nombre = models.CharField(max_length=100)
    fecha_añadido = models.DateField(null=True, blank=True)



    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s' % (self.nombre)
