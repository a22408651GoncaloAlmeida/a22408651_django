from django.contrib import admin
from .models import MakingOf, RegistoPapel, DecisaoModelacao, ErroCorrecao, UsoIA

class RegistoPapelInline(admin.TabularInline):
    model = RegistoPapel
    extra = 1

class DecisaoInline(admin.TabularInline):
    model = DecisaoModelacao
    extra = 1

class ErroInline(admin.TabularInline):
    model = ErroCorrecao
    extra = 1

class UsoIAInline(admin.TabularInline):
    model = UsoIA
    extra = 1

@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    inlines = [RegistoPapelInline, DecisaoInline, ErroInline, UsoIAInline]
    list_display = ['entidade', 'titulo', 'data']
    list_filter = ['entidade']