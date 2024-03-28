from rest_framework import serializers
from core import models
# import utils.constants import convert

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estado
        fields = '__all__'

    
class NivelPoluicaoSerializer(serializers.ModelSerializer):
    estado = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    status_choices = serializers.SerializerMethodField()
    
    def get_estado(self, obj):
        return {
            "nome": obj.estado.nome,
            "latitude": obj.estado.latitude,
            "longitude": obj.estado.longitude,
            "img_url": obj.estado.imagem_url
        }
    
    def get_status(self, obj):
        STATUS_DICT = {
            "P": "Pobre",
            "MP": "Muito Pobre",
            "B": "Bom",
            "M": "Moderado",
            "R": "Razoável"
        }
        status = STATUS_DICT.get(obj.status)
        return status
    
    def get_status_choices(self, obj):
        return obj.status
    class Meta:
        model = models.NivelPoluicao
        fields = '__all__'
