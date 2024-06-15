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
            'deslocamentos',
            'id_pokemon'
        )

class GolpesNaturaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = GolpesNaturais
        fields = (
            '__all__'
        )

class AtributosBasaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = AtributosBasais
        fields = (
            '__all__'
        )

class TiposHabilidadesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TiposHabilidades
        fields = (
            '__all__'
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
            '__all__'
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