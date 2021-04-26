from django.db import models


class CadastroDeProdutos(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome do Produto', unique=True)
    dataCadastro = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def get_dataCadastro(self):
        return self.dataCadastro.strftime('%d/%m/%Y')

    class Meta:
        ordering = ['nome', '-dataCadastro']
        verbose_name = 'Cadastro de Produto'
        verbose_name_plural = 'Cadastro de Produtos'


class CompraDeProdutos(models.Model):
    produto = models.ForeignKey('CadastroDeProdutos', on_delete=models.CASCADE, verbose_name='Produto')
    quantidade = models.PositiveIntegerField(default=1, verbose_name='Quantidade')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    preco_medio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço Medio de Compra')
    dataCompra = models.DateField(auto_now_add=True, verbose_name='Data de Compra')

    def __str__(self):
        return str(self.produto)

    def get_dataCompra(self):
        return self.dataCompra.strftime('%d/%m/%Y')

    # def CompraDeProdutoList2(request):
    #     media = CompraDeProdutos.objects.aggregate(media_preco=AVG(F('produto') * F('preco')))
    #     dados = {
    #         'produtos': media
    #     }
    #     super(dados).save()


    class Meta:
        ordering = ['produto', '-preco']
        verbose_name = 'Compra de Produto'
        verbose_name_plural = 'Compra de Produtos'

