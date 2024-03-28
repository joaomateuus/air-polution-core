from rest_framework import viewsets
from core import models
from core import serializers
from rest_framework import permissions

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = models.Estado.objects.all()
    serializer_class = serializers.EstadoSerializer
    permission_classes = (permissions.IsAuthenticated,)


class NivelPoluicaoViewSet(viewsets.ModelViewSet):
    queryset = models.NivelPoluicao.objects.all()
    serializer_class = serializers.NivelPoluicaoSerializer
    permission_classes = (permissions.IsAuthenticated,)