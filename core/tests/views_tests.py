from django.test import TestCase, Client
from django.urls import reverse


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def tearDown(self):
        pass


class ContatoViewTestCase(TestCase):
    def setUpClass(self):
        self.client = Client()
        self.url = reverse('contato')

    def test_form(self):
        data = {'nome': '', 'email': '', 'mensagem': ''}
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'contato_form', 'nome', 'Este campo é obrigatório.')
        self.assertFormError(response, 'contato_form', 'email', 'Este campo é obrigatório.')
        self.assertFormError(response, 'contato_form', 'mensagem', 'Este campo é obrigatório.')
