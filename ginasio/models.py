from django.db import models

# Create your models here.
class PersonalTrainer(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100, blank=True)
    biografia = models.TextField(blank=True)

    def __str__(self):
        return f"PT: {self.nome}"

class Membro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_inscricao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

class SessaoTreino(models.Model):
    personal_trainer = models.ForeignKey(
        PersonalTrainer, 
        on_delete=models.CASCADE,
        related_name='sessoes'
    )
    membro = models.ForeignKey(
        Membro, 
        on_delete=models.CASCADE, 
        related_name='treinos_agendados'
    )
    
    data = models.DateField()
    hora = models.TimeField()

    class Meta:
        # Garante que um PT não tenha dois agendamentos no mesmo horário e dia
        unique_together = ('personal_trainer', 'data', 'hora')

    def __str__(self):
        return f"Treino: {self.membro} com {self.personal_trainer} em {self.data} às {self.hora}"
