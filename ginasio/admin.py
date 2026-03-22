from django.contrib import admin
from .models import PersonalTrainer, Membro, SessaoTreino

admin.site.register(PersonalTrainer)
admin.site.register(Membro)
admin.site.register(SessaoTreino)