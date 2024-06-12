from rest_framework import serializers
from .models import Pokemon, Capacidades, Deslocamento, GolpesNaturais, AtributosBasais, TiposHabilidades, Comportamento, Narrador, Medidas, Procriacao

class PokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = (
            'id',
            'nome_pokemon',
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

class GolpesNaturaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = GolpesNaturais
        fields = (
            'evolucao',
            'golpe_01',
            'golpe_02',
            'id_pokemon'
        )

class AtributosBasaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = AtributosBasais
        fields = (
            'nome_atributo',
            'nome_pokemon_01',
            'nome_pokemon_02', 
            'atributo_01',
            'atributo_02',
            'id_pokemon'
        )

class TiposHabilidadesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TiposHabilidades
        fields = (
            'tipo_01',
            'tipo_02',
            'habilidade_01',
            'habilidade_02'
            'id_pokemon'
        )

class ComportamentoSerializer(serializers.ModelSerializer):

    class Meta:
        mdoel = Comportamento
        fields = (
            'dieta_01', 
            'dieta_02',
            'habitat_01',
            'habitat_02',
            'id_pokemon'
        )

class NarradorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Narrador
        fields = (
            'chance_captura',
            'experience',
            'id_pokemon'
        )

class MedidasSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Medidas
        fields = (
            'tamanho_01',
            'tamanho_02',
            'categoria_01', 
            'categoria_02',
            'id_pokemon'
        )

class ProcriacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Procriacao
        fields = (
            'sexo',
            'grupo_reprodutivo',
            'incubacao',
            'id_pokemon'
        )