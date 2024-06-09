from rest_framework import serializers
from .models import Pokemon, Capacidades, Deslocamento, GolpesNaturais, AtributosBasais, TiposHabilidades, Comportamento, Narrador, Medidas, Procriacao

class PokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = (
            'id',
            'nome'
            'imagem'
        )
