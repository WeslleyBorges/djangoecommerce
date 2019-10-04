# coding=utf-8

from django.shortcuts import render


def index(request):
    text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    text = text.replace(',', '')
    text = text.split(' ')
    return render(request, 'index.html', {'title': 'django e-commerce', 'text': text})
