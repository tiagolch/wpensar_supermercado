from django.contrib import admin

from .models import CompraDeProdutos, CadastroDeProdutos


@admin.register(CadastroDeProdutos)
class CadastroProdutosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'get_dataCadastro', 'ativo']
    list_filter = ['nome', 'dataCadastro', 'ativo']
    list_editable = ['ativo']
    list_per_page = 10
    search_fields = ['nome']


@admin.register(CompraDeProdutos)
class CompraDeProdutosAdmin(admin.ModelAdmin):
    list_filter = ['dataCompra']
    list_display = ['produto', 'quantidade', 'preco', 'get_dataCompra']
    search_fields = ['produto']
    list_per_page = 10