from django.db import models

# Create your models here.
class Produtos(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    preco = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    descricao = models.CharField(max_length=300, null=False, blank=False)
    quantidade = models.IntegerField()
