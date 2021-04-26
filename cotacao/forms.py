from django.forms import ModelForm
from .models import CompraDeProdutos, CadastroDeProdutos


class CadastroDeProdutosForm(ModelForm):
    class Meta:
        model = CadastroDeProdutos
        fields = ['nome',]


class CompraDeProdutosForm(ModelForm):
    class Meta:
        model = CompraDeProdutos
        fields = ['produto', 'quantidade', 'preco']
