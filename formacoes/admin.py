from django.contrib import admin
from .models import Formacao

@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'instituicao', 'tipo', 'data_inicio', 'data_fim']
    list_filter = ['tipo']