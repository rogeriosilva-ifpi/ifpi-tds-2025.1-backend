from django.db import models

class Produto(models.Model):
  nome = models.CharField(verbose_name='Nome', 
                          null=False, blank=False,
                          max_length=250)
  valor = models.DecimalField(verbose_name='Valor',
                              null=False, blank=False,
                              max_digits=6, decimal_places=2)
  disponivel = models.BooleanField(verbose_name='Disponível',
                                   null=False, blank=False,
                                   default=True)
  observacao = models.CharField(verbose_name='Observação',
                                blank=True, null=True,
                                max_length=500)
