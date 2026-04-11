from django.db import models
from tecnologias.models import Tecnologia

class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    repositorio = models.URLField(blank=True)
    destaque = models.BooleanField(default=False)
    classificacao = models.IntegerField(choices=[
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ], default=3)
    tecnologias = models.ManyToManyField(
        Tecnologia,
        related_name='tfcs',
        blank=True
    )

    def __str__(self):
        return self.titulo