from django.db import models

# Create your models here.
class Genero(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Banda (models.Model):
    nome = models.CharField(max_length=50)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='Género')

    def __str__(self):
        return self.nome

class Festival(models.Model):
    nome = models.CharField(max_length=30)
    banda = models.ManyToManyField(Banda, related_name='Bandas')

    def __str__(self):
        return self.nome