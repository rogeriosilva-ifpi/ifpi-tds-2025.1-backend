from django.db import models

class Estado(models.Model):
  nome = models.CharField(max_length=250, null=False, blank=False)
  sigla = models.CharField(max_length=2, null=False, blank=False)

  def __str__(self):
    return self.nome
  

class Cidade(models.Model):
  nome = models.CharField(max_length=250, null=False, blank=False)

  estado = models.ForeignKey(Estado, 
                             on_delete=models.SET_NULL,
                             null=True, blank=True,
                             related_name='cidades')
  
  def __str__(self):
    return f'{self.nome} - {self.estado.sigla}'
