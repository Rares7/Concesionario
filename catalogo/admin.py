from django.contrib import admin

# Register your models here.
from .models import Ciudad, Modelo, Marca, BookInstance

admin.site.register(Modelo)
admin.site.register(Marca)
admin.site.register(Ciudad)
admin.site.register(BookInstance)