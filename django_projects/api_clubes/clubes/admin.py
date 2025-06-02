from django.contrib import admin
from clubes.models import Clube, Jogador


class ClubeAdmin(admin.ModelAdmin):
  list_display = ['nome', 'uf', 'tem_estadio', 'data_fundacao']
  list_filter = ['uf']
  search_fields = ['nome',]


admin.site.register(Clube, ClubeAdmin)


class JogadorAdmin(admin.ModelAdmin):
  list_display = ['nome',]
  search_fields = ('nome',)


admin.site.register(Jogador, JogadorAdmin)
