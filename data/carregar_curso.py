import os
import sys
import django
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from portfolio.models import Licenciatura, UnidadeCurricular

# Criar a licenciatura LEI se não existir
licenciatura, _ = Licenciatura.objects.get_or_create(
    sigla='LEI',
    defaults={
        'nome': 'Licenciatura em Engenharia Informática',
        'ects_totais': 180,
        'duracao_anos': 3,
        'regime': 'presencial',
    }
)

FILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'files')

# Ler o ficheiro do curso para obter a lista de UCs
with open(os.path.join(FILES_DIR, 'ULHT260-PT.json'), encoding='utf-8') as f:
    curso = json.load(f)

ucs_carregadas = 0
ucs_erros = 0

for uc in curso['courseFlatPlan']:
    codigo = uc['curricularIUnitReadableCode']
    filepath = os.path.join(FILES_DIR, f'{codigo}-PT.json')

    if not os.path.exists(filepath):
        print(f"Ficheiro não encontrado: {filepath}")
        ucs_erros += 1
        continue

    with open(filepath, encoding='utf-8') as f:
        dados = json.load(f)

    if dados.get('errorCode') != '0':
        print(f"Erro na UC {codigo}: errorCode={dados.get('errorCode')}")
        ucs_erros += 1
        continue

    semestre_raw = uc.get('semester', uc.get('semestre', 1))
    semestre = int(semestre_raw) if str(semestre_raw).isdigit() else 1

    obj, created = UnidadeCurricular.objects.update_or_create(
        codigo=codigo,
        defaults={
            'nome': dados.get('curricularUnitName', ''),
            'sigla': dados.get('curricularIUnitReadableCode', codigo),
            'ects': dados.get('ects') or 0,
            'ano': dados.get('curricularYear') or 1,
            'semestre': semestre,
            'natureza': dados.get('nature', ''),
            'lingua': dados.get('language', ''),
            'objetivos': dados.get('objectives', ''),
            'programa': dados.get('programme', ''),
            'metodologia': dados.get('methodology', ''),
            'bibliografia': dados.get('bibliography', ''),
            'licenciatura': licenciatura,
        }
    )

    status = "Criada" if created else "Atualizada"
    print(f"[{status}] {codigo} — {dados.get('curricularUnitName', '?')}")
    if created:
        ucs_carregadas += 1

print(f"\n✅ {ucs_carregadas} UCs criadas | ⚠️ {ucs_erros} erros")