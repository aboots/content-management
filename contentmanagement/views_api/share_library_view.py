from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotFound, NotAcceptable
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from contentmanagement.models import User, Library
from contentmanagement.serializers import LibrarySerializer
from contentmanagement.views_api.token_view_set import TokenBaseApiView


class ShareLibraryView(TokenBaseApiView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = self.request.data
        if 'username' not in data or 'library' not in data:
            raise NotAcceptable('you should send username and library')
        username = data['username']
        library = data['library']
        library = Library.objects.filter(pk=library).first()
        owner = self.get_user()
        if owner.pk != library.owner.pk:
            raise NotAcceptable('this library does not belong to this user')
        user = User.objects.filter(username=username).first()
        if not user:
            raise NotFound('user not found')
        if user not in library.users.all():
            library.users.add(user)
            library.save()
        return Response(LibrarySerializer(instance=library).data)
