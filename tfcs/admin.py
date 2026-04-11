from django.contrib import admin
from .models import TFC

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autores', 'orientador', 'licenciatura', 'classificacao', 'destaque']
    list_filter = ['classificacao', 'destaque']