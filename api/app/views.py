from django.shortcuts import render

from app.models import Produtos
from app.serializers import ProdutosSerializer

from rest_framework import viewsets 


class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
