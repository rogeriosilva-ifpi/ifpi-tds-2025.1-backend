from django.contrib import admin
from core.models import Estado, Cidade


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
  list_display = ['nome', 'estado']


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
  list_display = ['nome', 'sigla']
