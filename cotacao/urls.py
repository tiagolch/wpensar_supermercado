from django.urls import path
from django.views.generic import TemplateView
from .views import CadastroDeProdutoList, CadastroDeProdutoNovo, CadastroDeProdutoAtualiza, CadastroDeProdutoDeleta


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('listagemCadastroProdutos/', CadastroDeProdutoList, name='listagemCadastroProdutos'),
    path('novoCadastroProdutos/', CadastroDeProdutoNovo, name='NovoCadastroProdutos'),
    path('atualizaCadastroProdutos/<int:id>/', CadastroDeProdutoAtualiza, name='atualizaCadastroProdutos'),
    path('deleteCadastroProdutos/<int:id>/', CadastroDeProdutoDeleta, name='deleteCadastroProdutos'),
]