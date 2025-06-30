from django.urls import path
from .views import hello, listar_clubes, ClubeView


urlpatterns = [
  path('', ClubeView.as_view()),
  path('hello/', hello),
  path('list-clubes/', listar_clubes)
]