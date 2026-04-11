from django.contrib import admin
from .models import Licenciatura, Docente, UnidadeCurricular

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla', 'ects_totais', 'duracao_anos', 'regime']

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'pagina_lusofona']

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla', 'ano', 'semestre', 'ects', 'licenciatura']
    list_filter = ['ano', 'semestre', 'licenciatura']