import json

from rest_framework.exceptions import ValidationError

from contentmanagement.models import LibraryFile
from contentmanagement.serializers.attachment_serializer import AttachmentModelSerializer
from contentmanagement.serializers.base_token_serializer import BaseTokenSerializer


class LibraryFileSerializer(BaseTokenSerializer):
    user_field_name = 'library__users'
    attachments = AttachmentModelSerializer(
        many=True,
        read_only=True
    )

    def validate(self, attrs):
        library = attrs['library']
        if library.owner.pk != self.context['user']:
            raise ValidationError('Not your own library')
        file_attributes = json.loads(library.file_attributes) \
            if library.file_attributes else list()
        if 'attributes' in attrs and not \
                set(json.loads(attrs['attributes']).keys()).issubset(set(file_attributes)):
            raise ValidationError('Not valid attribute.')
        return attrs

    def to_representation(self, instance):
        data = super(LibraryFileSerializer, self).to_representation(instance)
        data['attributes'] = json.loads(data['attributes']) \
            if data['attributes'] else data['attributes']
        data['attachment_fields'] = json.loads(data['attachment_fields']) \
            if data['attachment_fields'] else data['attachment_fields']
        return data

    def to_internal_value(self, data):
        if 'attributes' in data:
            data['attributes'] = json.dumps(data['attributes'])
        if 'attachment_fields' in data:
            data['attachment_fields'] = json.dumps(data['attachment_fields'])
        return super(LibraryFileSerializer, self).to_internal_value(data)

    class Meta:
        model = LibraryFile
        fields = (
            'id',
            'library',
            'file',
            'description',
            'attributes',
            'attachment_fields',
            'file_name',
            'created',
            'modified',
            'attachments'
        )

        read_only_fields = ('id', 'created', 'modified', 'file_name', 'attachments')
