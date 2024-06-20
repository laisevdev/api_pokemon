from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PokemonViewSet, CapacidadesViewSet, ComportamentoViewSet, TiposHabilidadesViewSet, DeslocamentoViewSet, GolpesNaturaisViewSet, AtributosBasaisViewSet, NarradorViewSet, MedidasViewSet, ProcriacaoViewSet

router = DefaultRouter()
router.register(r'pokemons', PokemonViewSet)
router.register(r'capacidades', CapacidadesViewSet)
router.register(r'comportamentos', ComportamentoViewSet)
router.register(r'tiposhabilidades', TiposHabilidadesViewSet)
router.register(r'deslocamentos', DeslocamentoViewSet)
router.register(r'golpes', GolpesNaturaisViewSet)
router.register(r'atributos', AtributosBasaisViewSet)
router.register(r'narrador', NarradorViewSet)
router.register(r'medidas', MedidasViewSet)
router.register(r'procriacao', ProcriacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

