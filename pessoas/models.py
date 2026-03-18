from django.db import models

# Create your models here.
class Pessoa (models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return f'{self.nome}: {self.idade} anos'


# Escola
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

# Ginásio
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


# Receita
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


# Loja
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.CharField(max_length=10)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    morada = models.CharField(max_length=200) # Morada única aqui mesmo

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} de {self.cliente.nome}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"