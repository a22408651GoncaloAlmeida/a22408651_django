# portfolio/admin.py
from django.contrib import admin
from .models import (
    Tecnologia, Projeto, Competencia, Conquista,
    Formacao,
    Licenciatura, Docente, UnidadeCurricular,
    TFC,
)

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'nivel_interesse', 'destaque')
    list_filter = ('categoria', 'nivel_interesse')
    search_fields = ('nome',)


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'unidade_curricular')
    list_filter = ('ano',)
    search_fields = ('nome',)
    filter_horizontal = ('tecnologias',)


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'nivel')
    list_filter = ('tipo', 'nivel')
    search_fields = ('nome',)
    filter_horizontal = ('tecnologias', 'projetos')


@admin.register(Conquista)
class ConquistaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'data', 'entidade_organizadora')
    list_filter = ('tipo',)
    search_fields = ('titulo',)
    filter_horizontal = ('competencias',)


@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'tipo', 'data_inicio', 'data_fim')
    list_filter = ('tipo',)
    search_fields = ('nome', 'instituicao')
    filter_horizontal = ('competencias',)


@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'ects_totais', 'duracao_anos', 'regime')
    list_filter = ('regime',)


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'pagina_lusofona')
    search_fields = ('nome', 'email')


@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'ano', 'semestre', 'ects', 'licenciatura')
    list_filter = ('ano', 'semestre', 'licenciatura')
    search_fields = ('nome', 'sigla', 'codigo')
    filter_horizontal = ('docentes',)

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autores', 'orientador', 'licenciatura', 'destaque', 'classificacao')
    list_filter = ('destaque', 'classificacao', 'licenciatura')
    search_fields = ('titulo', 'autores', 'orientador')
    filter_horizontal = ('tecnologias',)