from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from contentmanagement.views_api.token_view_set import TokenBaseApiView


class LogoutView(TokenBaseApiView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = self.get_user()
        user.token = None
        user.save()
        return Response('done')
