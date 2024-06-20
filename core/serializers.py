from rest_framework import serializers
from .models import Pokemon, Capacidades, Deslocamento, GolpesNaturais, AtributosBasais, TiposHabilidades, Comportamento, Narrador, Medidas, Procriacao

class PokemonSerializer(serializers.ModelSerializer):
    imagem = serializers.SerializerMethodField()

    class Meta:
        model = Pokemon
        fields = [
            'id',
            'nome_pokemon',
            'imagem'
        ]

    def get_imagem(self, obj):
        request = self.context.get('request')
        if obj.imagem and request:
            return request.build_absolute_uri(obj.imagem.url)
        return None

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
            'saude', 
            'ataque', 
            'defesa',
            'ataque_especial', 
            'defesa_especial',
            'velocidade',
            'id_pokemon'
        )

class TiposHabilidadesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TiposHabilidades
        fields = (
            '__all__'
        )

class ComportamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comportamento
        fields = (
            '__all__'
        )

class NarradorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Narrador
        fields = (
            'chance_captura',
            'experiencia',
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