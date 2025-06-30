from rest_framework.serializers import ModelSerializer
from .models import Clube

class ClubeSerializer(ModelSerializer):
  
  class Meta:
    model = Clube
    # fields = ['id', 'nome', 'tem_estadio']
    fields = '__all__'