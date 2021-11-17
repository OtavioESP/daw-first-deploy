from rest_framework import serializers

from app.models import Produtos


class ProdutosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Produtos
        fields = [
            'nome',
            'preco',
            'descricao',
            'quantidade'
        ]
