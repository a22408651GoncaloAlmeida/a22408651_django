from django.db import models
from tecnologias.models import Tecnologia

class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.CharField(max_length=200, default='')
    orientador = models.CharField(max_length=200, blank=True, default='')
    licenciatura = models.CharField(max_length=200, blank=True, default='')
    link_pdf = models.URLField(blank=True, default='')
    imagem = models.URLField(blank=True, default='')
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