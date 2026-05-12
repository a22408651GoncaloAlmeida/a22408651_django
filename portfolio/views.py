from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm
from .models import (
    Tecnologia, Projeto, Competencia, Conquista,
    Formacao, Licenciatura, Docente, UnidadeCurricular, TFC
)

# ── INDEX ──────────────────────────────────────────────────────────────────
def index_view(request):
    return render(request, 'portfolio/index.html', {})

# ── TECNOLOGIAS ────────────────────────────────────────────────────────────
def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})

def tecnologia_criar(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Nova Tecnologia'})

def tecnologia_editar(request, pk):
    tecnologia = get_object_or_404(Tecnologia, pk=pk)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=tecnologia)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Editar Tecnologia'})

def tecnologia_apagar(request, pk):
    tecnologia = get_object_or_404(Tecnologia, pk=pk)
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('tecnologias')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': tecnologia, 'titulo': 'Apagar Tecnologia'})

# ── PROJETOS ───────────────────────────────────────────────────────────────
def projetos_view(request):
    projetos = Projeto.objects.select_related('unidade_curricular').prefetch_related('tecnologias').all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def projeto_criar(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Novo Projeto'})

def projeto_editar(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Editar Projeto'})

def projeto_apagar(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': projeto, 'titulo': 'Apagar Projeto'})

# ── COMPETÊNCIAS ───────────────────────────────────────────────────────────
def competencias_view(request):
    competencias = Competencia.objects.all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

def competencia_criar(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Nova Competência'})

def competencia_editar(request, pk):
    competencia = get_object_or_404(Competencia, pk=pk)
    form = CompetenciaForm(request.POST or None, instance=competencia)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Editar Competência'})

def competencia_apagar(request, pk):
    competencia = get_object_or_404(Competencia, pk=pk)
    if request.method == 'POST':
        competencia.delete()
        return redirect('competencias')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': competencia, 'titulo': 'Apagar Competência'})


# ── FORMAÇÕES ──────────────────────────────────────────────────────────────
def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})

def formacao_criar(request):
    form = FormacaoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Nova Formação'})

def formacao_editar(request, pk):
    formacao = get_object_or_404(Formacao, pk=pk)
    form = FormacaoForm(request.POST or None, request.FILES or None, instance=formacao)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/form.html', {'form': form, 'titulo': 'Editar Formação'})

def formacao_apagar(request, pk):
    formacao = get_object_or_404(Formacao, pk=pk)
    if request.method == 'POST':
        formacao.delete()
        return redirect('formacoes')
    return render(request, 'portfolio/confirmar_apagar.html', {'objeto': formacao, 'titulo': 'Apagar Formação'})


# ── RESTANTES ────────────────────────────────────────────────

def conquistas_view(request):
    conquistas = Conquista.objects.all()
    return render(request, 'portfolio/conquistas.html', {'conquistas': conquistas})

def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.all()
    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})

def docentes_view(request):
    docentes = Docente.objects.all()
    return render(request, 'portfolio/docentes.html', {'docentes': docentes})

def ucs_view(request):
    ucs = UnidadeCurricular.objects.select_related('licenciatura').all()
    return render(request, 'portfolio/ucs.html', {'ucs': ucs})

def tfcs_view(request):
    tfcs = TFC.objects.prefetch_related('tecnologias').all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})