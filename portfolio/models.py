from django.db import models

# Create your models here.
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

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    imagem = models.ImageField(upload_to='projetos/', blank=True)
    video_demo = models.URLField(blank=True)
    repositorio_github = models.URLField(blank=True)
    ano = models.IntegerField()
    unidade_curricular = models.ForeignKey(
        'UnidadeCurricular',
        on_delete=models.SET_NULL,
        null=True,
        related_name='projetos'
    )
    tecnologias = models.ManyToManyField(
        'Tecnologia',
        related_name='projetos',
        blank=True
    )

    def __str__(self):
        return self.nome

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
        'Tecnologia',
        blank=True,
        related_name='competencias'
    )
    projetos = models.ManyToManyField(
        'Projeto',
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


class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)
    ects_totais = models.IntegerField()
    duracao_anos = models.IntegerField()
    regime = models.CharField(max_length=20, choices=[
        ('presencial', 'Presencial'),
        ('elearning', 'E-Learning'),
        ('misto', 'Misto'),
    ])

    def __str__(self):
        return self.sigla

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True)
    pagina_lusofona = models.URLField(blank=True)

    def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=20, blank=True)
    codigo = models.CharField(max_length=20, blank=True)   # ex: ULHT260-1
    ects = models.IntegerField()
    ano = models.IntegerField()
    semestre = models.IntegerField(default=1)
    natureza = models.CharField(max_length=50, blank=True)  # Mandatory/Optional
    lingua = models.CharField(max_length=50, blank=True)
    objetivos = models.TextField(blank=True)
    programa = models.TextField(blank=True)
    metodologia = models.TextField(blank=True)
    bibliografia = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='ucs/', blank=True)
    licenciatura = models.ForeignKey(
        Licenciatura,
        on_delete=models.CASCADE,
        related_name='unidades_curriculares'
    )
    docentes = models.ManyToManyField(
        Docente,
        related_name='unidades_curriculares',
        blank=True
    )

    def __str__(self):
        return self.nome

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