from rest_framework import serializers

from herois.models import Universo, Heroi, Habilidade, Categoria


class UniversoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universo
        fields = ('__all__')


class HabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidade
        fields = ('id', 'nome')


class HabilidadeDTOSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(read_only=True)


class HeroiSerializer(serializers.ModelSerializer):
    habilidade = HabilidadeDTOSerializer(many=True)
    class Meta:
        model = Heroi
        fields = ('__all__')


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')

