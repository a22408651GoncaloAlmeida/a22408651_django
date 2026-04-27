import os
import sys
import django
import json

# Configurar o Django
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from portfolio.models import TFC

# Caminho para o ficheiro JSON
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, 'tfcs_2025.json')

# Ler o JSON
with open(json_path, encoding='utf-8') as f:
    tfcs = json.load(f)

# Carregar os dados
criados = 0
for item in tfcs:
    tfc, created = TFC.objects.get_or_create(
        titulo=item['titulo'],
        defaults={
            'autores': item.get('autores', ''),
            'orientador': item.get('orientador', ''),
            'licenciatura': item.get('licenciatura', ''),
            'link_pdf': item.get('link_pdf', ''),
            'imagem': item.get('imagem', ''),
            'classificacao': item.get('rating', 3),
            'destaque': item.get('rating', 1) >= 4,
        }
    )
    if created:
        criados += 1

print(f"{criados} TFCs carregados com sucesso!")