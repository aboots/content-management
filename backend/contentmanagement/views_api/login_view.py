from django.contrib.auth.hashers import check_password
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotFound, PermissionDenied, NotAcceptable
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from contentmanagement.models import User
from contentmanagement.serializers import UserSerializer


class LoginView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = self.request.data
        if 'username' not in data or 'password' not in data:
            raise NotAcceptable('you should send password and username')
        username = data['username']
        password = data['password']
        user = User.objects.filter(username=username).first()
        if not user:
            raise NotFound('user not found')
        if user and (check_password(password, user.password) or password == user.password):
            user.set_token()
            user.save()
            return Response(UserSerializer(instance=user).data)
        raise PermissionDenied('password incorrect')
