import os
import sys
import django
import requests
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from licenciatura.models import Licenciatura, UnidadeCurricular

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

# Descarregar dados do curso
url_curso = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail'
payload = {'language': 'PT', 'courseCode': 260, 'schoolYear': '202526'}
headers = {'content-type': 'application/json'}
response = requests.post(url_curso, json=payload, headers=headers)
curso = response.json()

ucs_carregadas = 0

for uc in curso['courseFlatPlan']:
    codigo = uc['curricularIUnitReadableCode']

    # Descarregar detalhes da UC
    url_uc = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetSIGESCurricularUnitDetails'
    payload_uc = {'language': 'PT', 'curricularIUnitReadableCode': codigo}
    response_uc = requests.post(url_uc, json=payload_uc, headers=headers)
    dados = response_uc.json()

    if dados.get('errorCode') != '0':
        print(f"Erro na UC {codigo}")
        continue

    obj, created = UnidadeCurricular.objects.get_or_create(
        codigo=codigo,
        defaults={
            'nome': dados.get('curricularUnitName', ''),
            'sigla': codigo,
            'ects': dados.get('ects', 0),
            'ano': dados.get('curricularYear', 1),
            'semestre': 1,
            'natureza': dados.get('nature', ''),
            'lingua': dados.get('language', ''),
            'objetivos': dados.get('objectives', ''),
            'programa': dados.get('programme', ''),
            'metodologia': dados.get('methodology', ''),
            'bibliografia': dados.get('bibliography', ''),
            'licenciatura': licenciatura,
        }
    )

    if created:
        ucs_carregadas += 1
        print(f"UC carregada: {dados.get('curricularUnitName')}")

print(f"\n{ucs_carregadas} UCs carregadas com sucesso!")