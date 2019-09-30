from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from herois.models import Universo, Habilidade, Heroi, Categoria
from herois.serializers import UniversoSerializer, HabilidadeDTOSerializer, HabilidadeSerializer, HeroiSerializer, \
    CategoriaSerializer


class UniversoViewSets(viewsets.ModelViewSet):
    queryset = Universo.objects.all()
    serializer_class = UniversoSerializer


class HabilidadeViewSet(viewsets.ModelViewSet):
    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer


class HeroiViewSet(viewsets.ModelViewSet):
    queryset = Heroi.objects.all()
    serializer_class = HeroiSerializer


class CategoriaViewSets(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

