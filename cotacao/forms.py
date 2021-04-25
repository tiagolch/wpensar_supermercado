from django import forms
# from .models import CompraDeProdutos, CadastroDeProdutos


class CadastroDeProdutosForm(forms.ModelForm):
    nome = forms.CharField(required=True, initial='Nome do Produto')

