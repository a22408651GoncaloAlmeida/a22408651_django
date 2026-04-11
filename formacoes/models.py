from django.db import models
from competencias.models import Competencia

class Formacao(models.Model):
    TIPO_CHOICES = [
        ('academica', 'Académica'),
        ('curso', 'Curso Online'),
        ('certificacao', 'Certificação'),
        ('workshop', 'Workshop'),
    ]

    nome = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    descricao = models.TextField(blank=True)
    certificado = models.FileField(upload_to='certificados/', blank=True)
    competencias = models.ManyToManyField(
        Competencia,
        blank=True,
        related_name='formacoes'
    )

    class Meta:
        ordering = ['-data_inicio']

    def __str__(self):
        return self.nome