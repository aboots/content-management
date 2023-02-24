from contentmanagement.models import Attachment, Library
from contentmanagement.serializers import AttachmentSerializer
from contentmanagement.views_api.token_view_set import TokenModelViewSet


class AttachmentViewSet(TokenModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

    def filter_queryset(self, queryset):
        if 'library-file' in self.request.query_params:
            library_file_pk = self.request.query_params['library-file']
            queryset = queryset.filter(library_file__pk=library_file_pk)
        return queryset
