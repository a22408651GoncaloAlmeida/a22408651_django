from django.contrib import admin
from .models import Competencia, Conquista

@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'nivel']
    list_filter = ['tipo', 'nivel']

@admin.register(Conquista)
class ConquistaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'data', 'entidade_organizadora']
    list_filter = ['tipo']