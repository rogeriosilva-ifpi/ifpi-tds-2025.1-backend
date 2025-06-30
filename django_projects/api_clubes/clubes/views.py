from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from yaml import serialize
from .models import Clube
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ClubeSerializer

# DRF Views
class ClubeView(APIView):
  
  def get(self, request):
    # fazer algo...
    # clubes = [
    #   {'nome': 'CAP - Clube Atlético Piauiense', 'uf': 'PI'},
    #   {'nome': 'SEP - Sociedade Esportivo de Picos', 'uf': 'PI'},
    # ]
    clubes = Clube.objects.all()
    serializer = ClubeSerializer(clubes, many=True)
    return Response(data=serializer.data)


# Create your views here.
def hello(request):
  return HttpResponse('Hello Google')


def listar_clubes(request: HttpRequest):
  # logica, consulta a banco de dados nem nada
  quantidade = Clube.objects.count
  lista = Clube.objects.all()
  
  context = {
    'quantidade': quantidade,
    'lista': lista
    }
  
  return render(request, 'list_clubes.html', context)

