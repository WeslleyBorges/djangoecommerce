from django.shortcuts import render, get_object_or_404
from .models import Produto, Categoria
from django.views.generic import ListView, DetailView, View


# def produtos_categoria(request, slug):
#     categoria = Categoria.objects.get(slug=slug)
#     produtos_queryset = Produto.objects.filter(categoria=categoria)
#     context = {
#         'produtos': produtos_queryset,
#         'categoria': categoria
#     }
#     return render(request, 'catalogo/produtos_categoria.html', context)


class ProdutosCategoriaList(ListView):
    template_name = 'catalogo/produtos_categoria.html'
    model = Produto
    context_object_name = 'produtos'

    def get_queryset(self):
        categoria = get_object_or_404(Categoria, slug=self.kwargs['slug'])
        produtos_queryset = Produto.objects.filter(categoria=categoria)
        return produtos_queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = get_object_or_404(Categoria, slug=self.kwargs['slug'])
        return context


class ProdutoDetail(DetailView):
    model = Produto
    template_name = 'produto.html'
    context_object_name = 'produto'

    def get_context_data(self, **kwargs):
        slug = kwargs['object'].slug
        context = super().get_context_data(**kwargs)
        context['produto'] = Produto.objects.get(slug=slug)
        return context


class ProdutosList(ListView):
    model = Produto
    template_name = 'produtos.html'
    context_object_name = 'produtos'


produtos = ProdutosList.as_view()
produto = ProdutoDetail.as_view()
produtos_categoria = ProdutosCategoriaList.as_view()