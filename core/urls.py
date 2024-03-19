
from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()

router.register(r'bairros', viewsets.BairroViewSet, basename='bairros')
router.register(r'nivel_poluicao', viewsets.NivelPoluicaoViewSet, basename='nivel_poluicao')

urlpatterns = router.urls