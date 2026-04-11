from django.contrib import admin
from .models import TFC

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'ano', 'classificacao', 'destaque']
    list_filter = ['ano', 'classificacao', 'destaque']