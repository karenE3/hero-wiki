from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from herois.models import Universo, Habilidade,Heroi
from herois.serializers import UniversoSerializer


class UniversoViewSets(viewsets.ModelViewSet):
    queryset = Universo.objects.all()
    serializer_class = UniversoSerializer

class HabilidadeViewSet(viewsets.ModelViewSet):
    queryset = Habilidade.objects.all()
    serializer_class = Habilidade



class HeroiViewSet(viewsets.ModelViewSet):
    queryset = Heroi.objects.all()
    serializer_class = Heroi

