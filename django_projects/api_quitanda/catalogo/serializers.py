from rest_framework.serializers import ModelSerializer
from .models import Produto

class ProdutoSerializer(ModelSerializer):
  
  class Meta:
    model = Produto
    fields = ['id', 'nome', 'valor']