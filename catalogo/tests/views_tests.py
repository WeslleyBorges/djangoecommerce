from django.test import TestCase, Client
from django.urls import reverse
from model_mommy import mommy


class CategoriaTestCase(TestCase):
    def setUp(self):
        self.categoria = mommy.make('catalogo.Categoria')

    def test_get_absolute_url(self):
        self.assertEquals(self.categoria.get_absolute_url(),
                          reverse('produtos_categoria', kwargs={'slug': self.categoria.slug}))

    def tearDown(self):
        pass


class ProdutoTestCase(TestCase):
    def setUp(self):
        self.produto = mommy.make('catalogo.Produto', slug='produto')

    def test_get_absolute_url(self):
        self.assertEquals(self.produto.get_absolute_url(),
                          reverse('produto', kwargs={'slug': self.produto.slug}))