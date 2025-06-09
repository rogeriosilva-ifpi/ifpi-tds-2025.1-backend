from django.contrib import admin
from django.urls import path, include
admin.site.site_header = 'Sistemas de Clubes de Futebol'
admin.site.index_title = 'Operações de Cadastro'


urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('painel/', admin.site.urls),
    path('clubes/', include('clubes.urls'))
]
