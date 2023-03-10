import json

from rest_framework.exceptions import ValidationError

from contentmanagement.models import Attachment
from contentmanagement.serializers.base_token_serializer import BaseTokenSerializer


class AttachmentSerializer(BaseTokenSerializer):
    user_field_name = 'library_file__library__users'

    def validate(self, attrs):
        library_file = attrs['library_file']
        if library_file.library.owner.pk != self.context['user']:
            raise ValidationError('Not your own library')
        fields = json.loads(library_file.attachment_fields) \
            if library_file.attachment_fields else list()
        if attrs['field'] not in fields:
            raise ValidationError('Not valid attachment field')
        return attrs

    class Meta:
        model = Attachment
        fields = (
            'id',
            'field',
            'library_file',
            'file',
            'file_name',
            'created',
            'modified'
        )

        read_only_fields = ('id', 'created', 'modified', 'file_name')
