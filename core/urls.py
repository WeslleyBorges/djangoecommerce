from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
    path('produtos/', produtos, name='produtos'),
]
