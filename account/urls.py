
from rest_framework.routers import DefaultRouter
from account import viewsets

router = DefaultRouter()

router.register(r'users', viewsets.UserViewSet, basename='users')

urlpatterns = router.urls