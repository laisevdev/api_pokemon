from rest_framework import viewsets
from .models import Pokemon, Capacidades, Comportamento, TiposHabilidades, Deslocamento, GolpesNaturais, AtributosBasais, Narrador, Medidas, Procriacao
from .serializers import PokemonSerializer, CapacidadesSerializer, ComportamentoSerializer, TiposHabilidadesSerializer, DeslocamentoSerializer, GolpesNaturaisSerializer, AtributosBasaisSerializer , NarradorSerializer, MedidasSerializer, ProcriacaoSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    
class CapacidadesViewSet(viewsets.ModelViewSet):
    queryset = Capacidades.objects.all()
    serializer_class = CapacidadesSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    
class ComportamentoViewSet(viewsets.ModelViewSet):
    queryset = Comportamento.objects.all()
    serializer_class = ComportamentoSerializer

    def get_serializer_context(self):
        return {'request': self.request}

#RESOLVER PROBLEM    
class TiposHabilidadesViewSet(viewsets.ModelViewSet):
    queryset = TiposHabilidades.objects.all()
    serializer_class = TiposHabilidadesSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    
class DeslocamentoViewSet(viewsets.ModelViewSet):
    queryset = Deslocamento.objects.all()
    serializer_class = DeslocamentoSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    
class GolpesNaturaisViewSet(viewsets.ModelViewSet):
    queryset = GolpesNaturais.objects.all()
    serializer_class = GolpesNaturaisSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    
class AtributosBasaisViewSet(viewsets.ModelViewSet):
    queryset = AtributosBasais.objects.all()
    serializer_class = AtributosBasaisSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    
class NarradorViewSet(viewsets.ModelViewSet):
    queryset = Narrador.objects.all()
    serializer_class = NarradorSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    
class MedidasViewSet(viewsets.ModelViewSet):
    queryset = Medidas.objects.all()
    serializer_class = MedidasSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    
class ProcriacaoViewSet(viewsets.ModelViewSet):
    queryset = Procriacao.objects.all()
    serializer_class = ProcriacaoSerializer

    def get_serializer_context(self):
        return {'request': self.request}
