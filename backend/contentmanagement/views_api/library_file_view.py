from contentmanagement.models import LibraryFile
from contentmanagement.serializers import LibraryFileSerializer
from contentmanagement.views_api.token_view_set import TokenModelViewSet


class LibraryFileModelViewSet(TokenModelViewSet):
    queryset = LibraryFile.objects.all()
    serializer_class = LibraryFileSerializer

    def filter_queryset(self, queryset):
        if 'library' in self.request.query_params:
            library_pk = self.request.query_params['library']
            queryset = queryset.filter(library__pk=library_pk)
        return queryset
