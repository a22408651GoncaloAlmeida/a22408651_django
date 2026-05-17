import os
import sys
import django
from django.core.files import File

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from portfolio.models import Tecnologia, Projeto, Conquista, UnidadeCurricular, Formacao
from artigos.models import Artigo
from escola.models import Curso

def migrar_imagens(modelo, campo_imagem):
    nome_modelo = modelo.__name__
    migrados = 0
    for obj in modelo.objects.all():
        imagem = getattr(obj, campo_imagem)
        if imagem and imagem.name:
            local_path = os.path.join('media', imagem.name)
            if os.path.exists(local_path):
                with open(local_path, 'rb') as f:
                    getattr(obj, campo_imagem).save(
                        os.path.basename(local_path),
                        File(f),
                        save=True
                    )
                migrados += 1
                print(f"Migrado: {obj}")
            else:
                print(f"Ficheiro não encontrado: {local_path}")
    print(f"\n{nome_modelo}: {migrados} imagens migradas\n")

migrar_imagens(Tecnologia, 'logo')
migrar_imagens(Projeto, 'imagem')
migrar_imagens(Conquista, 'imagem')
migrar_imagens(UnidadeCurricular, 'imagem')
migrar_imagens(Artigo, 'fotografia')
migrar_imagens(Curso, 'imagem')