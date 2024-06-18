from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pokemon
#Capacidades, Comportamento, Deslocamento, GolpesNaturais, AtributosBasais, TiposHabilidades, Narrador, Medidas, Procriacao 
from .serializers import PokemonSerializer
#CapacidadesSerializer, ComportamentoSerializer, DeslocamentoSerializer, GolpesNaturaisSerializer, AtributosBasaisSerializer, TiposHabilidadesSerializer, NarradorSerializer, MedidasSerializer, ProcriacaoSerializer

class PokemonAPIView(APIView):
    def get(self, request): 
        pokemons = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemons, many=True)
        return Response(serializer.data)