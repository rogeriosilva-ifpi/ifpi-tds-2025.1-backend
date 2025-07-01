from django.urls import path
from .views import ProdutoView

urlpatterns = [
    path('produtos/', ProdutoView.as_view()),
]