from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import Cidade, Estado

class CidadeSerializer(ModelSerializer):

  class Meta:
    model = Cidade
    fields = ['id', 'nome']


class EstadoSerializer(ModelSerializer):
  cidades = CidadeSerializer(many=True, read_only=True)

  class Meta:
    model = Estado
    fields = ['id', 'nome', 'sigla', 'cidades']