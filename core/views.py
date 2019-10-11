# coding=utf-8

from django.shortcuts import render
from .forms import ContatoForm
from django.views.generic import View


class IndexView(View):
    def get(self, request):
        text = '''Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt 
                      ut labore et dolore magna aliqua.'''
        text = text.replace(',', '')
        text = text.split(' ')
        context = {
            'title': 'django e-commerce',
            'text': text,
        }
        return render(request, 'index.html', context)


class ContatoView(View):
    def get(self, request):
        contato_form = ContatoForm()
        context = {
            'contato_form': contato_form
        }
        return render(request, 'contato.html', context)

    def post(self, request):
        contato_form = ContatoForm(request.POST)
        contato_form.send_mail()
        context = {
            'success': True
        }
        return render(request, 'contato.html', context)


index = IndexView.as_view()
contato = ContatoView.as_view()
