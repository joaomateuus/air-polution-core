from rest_framework import serializers
from core import models

class BairroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bairro
        fields = '__all__'


class NivelPoluicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NivelPoluicao
        fields = '__all__'
