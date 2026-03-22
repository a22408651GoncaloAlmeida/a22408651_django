from django.db import models

# Create your models here.
class Turma(models.Model):
    nome = models.CharField(max_length=50)
    ano_letivo = models.CharField(max_length=9)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=50, blank=True)
    turmas = models.ManyToManyField(
        Turma, 
        related_name='professores'
    )

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.ForeignKey(
        Turma, 
        on_delete=models.CASCADE, 
        related_name='alunos'
    )

    def __str__(self):
        return self.nome