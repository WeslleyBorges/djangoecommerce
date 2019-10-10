from django.shortcuts import render
from .models import Produto, Categoria


def produtos_categoria(request, slug):
    categoria = Categoria.objects.get(slug=slug)
    produtos_queryset = Produto.objects.filter(categoria=categoria)
    context = {
        'produtos': produtos_queryset,
        'categoria': categoria
    }
    return render(request, 'catalogo/produtos_categoria.html', context)


def produto(request, slug):
    produto_instance = Produto.objects.get(slug=slug)
    context = {
        'produto': produto_instance
    }
    return render(request, 'catalogo/produto.html', context)


def produtos(request):
    produtos_queryset = Produto.objects.all()
    context = {
        'produtos': produtos_queryset
    }
    return render(request, 'catalogo/produtos.html', context)