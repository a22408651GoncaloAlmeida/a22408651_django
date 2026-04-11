from django.db import models

class MakingOf(models.Model):
    ENTIDADE_CHOICES = [
        ('licenciatura', 'Licenciatura'),
        ('unidade_curricular', 'Unidade Curricular'),
        ('projeto', 'Projeto'),
        ('tecnologia', 'Tecnologia'),
        ('tfc', 'TFC'),
        ('competencia', 'Competência'),
        ('formacao', 'Formação'),
        ('makingof', 'Making Of'),
    ]

    entidade = models.CharField(max_length=30, choices=ENTIDADE_CHOICES)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_entidade_display()} — {self.titulo}"

class RegistoPapel(models.Model):
    making_of = models.ForeignKey(
        MakingOf,
        on_delete=models.CASCADE,
        related_name='registos_papel'
    )
    descricao = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='makingof/papel/')

    def __str__(self):
        return self.descricao

class DecisaoModelacao(models.Model):
    making_of = models.ForeignKey(
        MakingOf,
        on_delete=models.CASCADE,
        related_name='decisoes'
    )
    titulo = models.CharField(max_length=200)
    justificacao = models.TextField()

    def __str__(self):
        return self.titulo

class ErroCorrecao(models.Model):
    making_of = models.ForeignKey(
        MakingOf,
        on_delete=models.CASCADE,
        related_name='erros'
    )
    descricao_erro = models.TextField()
    correcao_aplicada = models.TextField()
    data = models.DateField()

    def __str__(self):
        return f"Erro em {self.making_of.entidade}: {self.descricao_erro[:50]}"

class UsoIA(models.Model):
    making_of = models.ForeignKey(
        MakingOf,
        on_delete=models.CASCADE,
        related_name='usos_ia'
    )
    ferramenta = models.CharField(max_length=100)
    descricao_uso = models.TextField()
    contribuicao = models.TextField()
    data = models.DateField()

    def __str__(self):
        return f"{self.ferramenta} — {self.making_of.entidade}"