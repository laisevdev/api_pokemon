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

class CapacidadesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Capacidades 
        fields = (
            'forca',
            'inteligencia',
            'salto',
            'outras',
            'id_pokemon'
        )

class DeslocamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deslocamento
        fields = (
            'terrestre',
            'escavacao', 
            'natacao',
            'subaquatico',
            'voo',
            'id_pokemon'
        )