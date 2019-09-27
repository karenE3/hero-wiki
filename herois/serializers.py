from rest_framework import serializers

from herois.models import Universo, Heroi, Habilidade


class UniversoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universo
        fields = ('__all__')


class HabilidadeDTOSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(read_only=True)

class HeroiSerializer(serializers.ModelSerializer):
    habilidade = HabilidadeDTOSerializer(many=True)
    class Meta:
        model = Heroi
        fields = ('nome', 'universo','idade','habilidade','categoria')