from django.urls import path
from .views import *

urlpatterns = [
    path('produtos/categoria/<slug:slug>/', produtos_categoria, name='produtos_categoria'),
    path('produto/<slug:slug>/', produto, name='produto'),
    path('produtos/', produtos, name='produtos'),
]
