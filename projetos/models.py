from django.db import models
from licenciatura.models import UnidadeCurricular
from tecnologias.models import Tecnologia

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    imagem = models.ImageField(upload_to='projetos/', blank=True)
    video_demo = models.URLField(blank=True)
    repositorio_github = models.URLField(blank=True)
    ano = models.IntegerField()
    unidade_curricular = models.ForeignKey(
        UnidadeCurricular,
        on_delete=models.SET_NULL,
        null=True,
        related_name='projetos'
    )
    tecnologias = models.ManyToManyField(
        Tecnologia,
        related_name='projetos',
        blank=True
    )

    def __str__(self):
        return self.nome