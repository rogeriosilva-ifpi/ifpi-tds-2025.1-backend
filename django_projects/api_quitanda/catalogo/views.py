from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Produto
from .serializers import ProdutoSerializer


class ProdutoView(APIView):

  def get(self, request):
    produtos = Produto.objects.all()
    serializer = ProdutoSerializer(produtos, many=True)
    return Response(data=serializer.data)