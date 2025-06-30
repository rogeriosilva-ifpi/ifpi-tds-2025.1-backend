import datetime
from django.db import models


class Clube(models.Model):
  nome = models.CharField()
  uf = models.CharField(max_length=2, null=True, blank=True)
  data_fundacao = models.DateField(default=datetime.datetime.today)
  tem_estadio = models.BooleanField(default=False)

  def __str__(self):
    return self.nome


class Jogador(models.Model):
  nome = models.CharField(null=False)

  # relacionamentos
  clube = models.ForeignKey(Clube, on_delete=models.SET_NULL, null=True)

  class Meta:
    verbose_name_plural = 'Jogadores'

  def __str__(self):
    return self.nome
