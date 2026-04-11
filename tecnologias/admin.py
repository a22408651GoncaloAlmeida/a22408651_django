from django.contrib import admin
from .models import Tecnologia

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'nivel_interesse']
    list_filter = ['categoria', 'nivel_interesse']