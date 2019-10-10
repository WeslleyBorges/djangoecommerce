from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=30)
    slug = models.SlugField(verbose_name='Identificador', max_length=100)

    created = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Modificado em', auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def get_absolute_url(self):
        return reverse('produtos_categoria', kwargs={'slug': self.slug})


class Produto(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=30)
    slug = models.SlugField(verbose_name='Identificador', max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.TextField(verbose_name='Descrição', blank=True)
    preco = models.DecimalField(verbose_name='Preço', decimal_places=2, max_digits=5)

    created = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Modificado em', auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Produtos'
        ordering = ['nome']

    def get_absolute_url(self):
        return reverse('produto', kwargs={'slug': self.slug})
