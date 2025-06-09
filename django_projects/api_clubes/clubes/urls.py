from django.urls import path
from .views import hello, listar_clubes


urlpatterns = [
  path('hello/', hello),
  path('list-clubes/', listar_clubes)
]