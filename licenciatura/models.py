from django.db import models

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