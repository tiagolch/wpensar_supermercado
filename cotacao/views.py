from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CompraDeProdutosForm, CadastroDeProdutosForm
from .models import CadastroDeProdutos


@login_required()
def CadastroDeProdutoList(request):
    produtos = CadastroDeProdutos.objects.all()
    dados = {
        'produtos': produtos
    }
    return render(request, 'cotacao/listagemCadastroProdutos.html', dados)


@login_required()
def CadastroDeProdutoNovo(request):
    form = CadastroDeProdutosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listagemCadastroProdutos')
    return render(request, 'cotacao/novoCadastroProdutos.html', {'form': form})


@login_required()
def CadastroDeProdutoAtualiza(request, id):
    produto =get_object_or_404(CadastroDeProdutos, pk=id)
    form = CadastroDeProdutosForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('listagemCadastroProdutos')
    return render(request, 'cotacao/novoCadastroProdutos.html', {'form': form})


@login_required()
def CadastroDeProdutoDeleta(request, id):
    produto = get_object_or_404(CadastroDeProdutos, pk=id)
    form = CadastroDeProdutosForm(request.POST or None, instance=produto)
    if request.method == 'POST':
        produto.delete()
        return redirect('listagemCadastroProdutos')
    return render(request, 'cotacao/confirmaDeleteCadastroProduto.html', {'form':form})


@login_required()
def index(request):
    return render(request, 'index.html')
