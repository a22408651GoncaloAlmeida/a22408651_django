from django.contrib import admin
from .models import Utilizador, Ingrediente, Receita

admin.site.register(Utilizador)
admin.site.register(Ingrediente)
admin.site.register(Receita)