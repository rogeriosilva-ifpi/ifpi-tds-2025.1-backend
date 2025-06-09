from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Clube


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

