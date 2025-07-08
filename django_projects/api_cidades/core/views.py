from rest_framework import viewsets
from .models import Estado
from .serializers import EstadoSerializer


class EstadoViewSet(viewsets.ModelViewSet):
  queryset = Estado.objects.all()
  serializer_class = EstadoSerializer
  