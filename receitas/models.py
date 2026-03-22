from django.db import models

# Create your models here.
class Utilizador(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Receita(models.Model):
    titulo = models.CharField(max_length=100)
    ingredientes = models.ManyToManyField(Ingrediente)
    favoritada_por = models.ManyToManyField(Utilizador, blank=True)

    def __str__(self):
        return self.titulo