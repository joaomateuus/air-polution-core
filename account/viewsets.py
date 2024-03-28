from rest_framework import viewsets
from account import models
from account import serializers
from account import permissions

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.UserPermissions,]

    def create(self, request, *args, **kwargs):
        try:
            print(request.data)
            return super().create(request, *args, **kwargs)
        except Exception as e:
            print(str(e))

