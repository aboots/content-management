from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from contentmanagement.models import User
from contentmanagement.serializers import UserSerializer
from contentmanagement.serializers.user_serializer import ListUserSerializer


class UserModelViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = User.objects.all()
    filter_backends = (DjangoFilterBackend,)

    def get_serializer_class(self):
        if self.action == 'list':
            return ListUserSerializer
        return UserSerializer
