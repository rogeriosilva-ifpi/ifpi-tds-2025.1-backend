from django.contrib import admin
from django.urls import path


admin.site.site_header = 'Sistemas de Clubes de Futebol'
admin.site.index_title = 'Operações de Cadastro'

urlpatterns = [
    path('painel/', admin.site.urls),
]
