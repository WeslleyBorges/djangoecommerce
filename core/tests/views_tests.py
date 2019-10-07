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

