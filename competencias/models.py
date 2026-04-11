from django.db import models
from tecnologias.models import Tecnologia
from projetos.models import Projeto

class Competencia(models.Model):
    TIPO_CHOICES = [
        ('tecnica', 'Técnica'),
        ('soft', 'Soft Skill'),
        ('linguistica', 'Linguística'),
    ]
    NIVEL_CHOICES = [
        (1, 'Básico'),
        (2, 'Intermédio'),
        (3, 'Avançado'),
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descricao = models.TextField(blank=True)
    nivel = models.IntegerField(choices=NIVEL_CHOICES, default=1)
    tecnologias = models.ManyToManyField(
        Tecnologia,
        blank=True,
        related_name='competencias'
    )
    projetos = models.ManyToManyField(
        Projeto,
        blank=True,
        related_name='competencias'
    )

    def __str__(self):
        return self.nome

class Conquista(models.Model):
    TIPO_CHOICES = [
        ('premio', 'Prémio'),
        ('hackathon', 'Hackathon'),
        ('mencao', 'Menção Honrosa'),
        ('participacao', 'Participação'),
    ]

    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descricao = models.TextField(blank=True)
    data = models.DateField()
    entidade_organizadora = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='conquistas/', blank=True)
    competencias = models.ManyToManyField(
        Competencia,
        blank=True,
        related_name='conquistas'
    )

    def __str__(self):
        return self.titulo