# coding=utf-8

from django.shortcuts import render
from catalogo.models import Produto, Categoria


def index(request):
    text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    text = text.replace(',', '')
    text = text.split(' ')
    context = {
        'title': 'django e-commerce',
        'text': text,
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, **kwargs):
    produto_instance = Produto.objects.get(pk=kwargs['id'])
    context = {
        'produto': produto_instance
    }
    return render(request, 'produto.html', context)


def produtos(request):
    produtos_queryset = Produto.objects.all()
    context = {
        'produtos': produtos_queryset
    }
    return render(request, 'produtos.html', context)
