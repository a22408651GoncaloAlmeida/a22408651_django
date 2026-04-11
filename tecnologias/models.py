from django.db import models

class Tecnologia(models.Model):
    CATEGORIA_CHOICES = [
        ('linguagem', 'Linguagem'),
        ('framework', 'Framework'),
        ('base_dados', 'Base de Dados'),
        ('devops', 'DevOps'),
        ('ferramenta', 'Ferramenta'),
    ]
    NIVEL_CHOICES = [
        (1, 'Iniciante'),
        (2, 'Básico'),
        (3, 'Intermédio'),
        (4, 'Avançado'),
        (5, 'Especialista'),
    ]

    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    descricao = models.TextField(blank=True)
    logo = models.ImageField(upload_to='tecnologias/', blank=True)
    website = models.URLField(blank=True)
    nivel_interesse = models.IntegerField(choices=NIVEL_CHOICES, default=3)
    destaque = models.TextField(blank=True)

    def __str__(self):
        return self.nome