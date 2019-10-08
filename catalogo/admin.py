from django.contrib import admin
from .models import Categoria


# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'created', 'modified']
    search_fields = ['nome', 'slug']


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'categoria', 'created', 'modified']
    search_fields = ['nome', 'slug', 'categoria__nome']
    list_filter = ['categoria']


admin.site.register(Categoria, CategoriaAdmin)
