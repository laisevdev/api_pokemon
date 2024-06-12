from django.urls import path
from .views import PokemonAPIView

urlpatterns = [
    path('pokemons/', PokemonAPIView.as_view(), name='pokemons')
]
