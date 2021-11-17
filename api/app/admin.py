from django.contrib import admin

from . import models

# Register your models here.
@admin.register(models.Produtos)
class AuthorAdmin(admin.ModelAdmin):
    fields = [
        'nome',
        'preco',
        'quantidade',
        'descricao',
    ]
    list_display = ['nome','preco','quantidade']
    list_filter = ['nome','preco','quantidade']
    ordering = ['nome']
    
