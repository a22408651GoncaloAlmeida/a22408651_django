from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User, Group
from .models import Artigo, Comentario
from .forms import ArtigoForm, ComentarioForm

def é_autor(user):
    return user.is_authenticated and (user.is_superuser or user.groups.filter(name='autores').exists())

def artigos_view(request):
    artigos = Artigo.objects.select_related('autor').prefetch_related('comentarios', 'likes').all()
    return render(request, 'artigos/artigos.html', {
        'artigos': artigos,
        'é_autor': é_autor(request.user),
    })

def artigo_detalhe(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    comentarios = artigo.comentarios.select_related('autor').all()
    form_comentario = ComentarioForm()

    if request.method == 'POST' and request.user.is_authenticated:
        form_comentario = ComentarioForm(request.POST)
        if form_comentario.is_valid():
            c = form_comentario.save(commit=False)
            c.artigo = artigo
            c.autor = request.user
            c.save()
            return redirect('artigo_detalhe', pk=pk)

    return render(request, 'artigos/artigo_detalhe.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form_comentario': form_comentario,
        'é_autor': é_autor(request.user),
        'já_deu_like': artigo.likes.filter(pk=request.user.pk).exists() if request.user.is_authenticated else False,
    })

@login_required
def artigo_like(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if artigo.likes.filter(pk=request.user.pk).exists():
        artigo.likes.remove(request.user)
    else:
        artigo.likes.add(request.user)
    return redirect('artigo_detalhe', pk=pk)

@login_required
def artigo_criar(request):
    if not é_autor(request.user):
        raise PermissionDenied
    form = ArtigoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect('artigos')
    return render(request, 'artigos/form.html', {'form': form, 'titulo': 'Novo Artigo'})

@login_required
def artigo_editar(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if artigo.autor != request.user and not request.user.is_superuser:
        raise PermissionDenied
    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('artigo_detalhe', pk=pk)
    return render(request, 'artigos/form.html', {'form': form, 'titulo': 'Editar Artigo'})

@login_required
def artigo_apagar(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if artigo.autor != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        artigo.delete()
        return redirect('artigos')
    return render(request, 'artigos/confirmar_apagar.html', {'objeto': artigo, 'titulo': 'Apagar Artigo'})