from django.urls import path
from catalogo.views import produtos_categoria

urlpatterns = [
    path('produtos/categoria/<int:id>/', produtos_categoria, name='produtos_categoria'),
]
