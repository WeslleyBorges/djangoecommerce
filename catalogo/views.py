from django.shortcuts import render
from catalogo.models import Produto


def produtos_categoria(request, **kwargs):
    produtos_queryset = Produto.objects.filter(categoria__pk=kwargs['id'])
    context = {
        'produtos': produtos_queryset
    }
    return render(request, 'produtos.html', context)
