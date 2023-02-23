from contentmanagement.models import Library
from contentmanagement.serializers import LibrarySerializer
from contentmanagement.views_api.token_view_set import TokenModelViewSet


class LibraryModelViewSet(TokenModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

    def get_queryset(self):
        query = super(TokenModelViewSet, self).get_queryset()
        user = self.get_user()
        return query.filter(users=user)
