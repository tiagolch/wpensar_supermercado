from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg, aggregates, Sum, F, Count,Q



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
    preco_medio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço Medio de Compra', blank=True, null=True)
    dataCompra = models.DateField(auto_now_add=True, verbose_name='Data de Compra')

    def __str__(self):
        return str(self.produto)

    def get_dataCompra(self):
        return self.dataCompra.strftime('%d/%m/%Y')

    def save(self, *args, **kwargs):
        preco_medio = CompraDeProdutos.objects.filter(produto=self.produto).aggregate(Avg('preco'))
        self.preco_medio=preco_medio['preco__avg']
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['produto', '-preco']
        verbose_name = 'Compra de Produto'
        verbose_name_plural = 'Compra de Produtos'

