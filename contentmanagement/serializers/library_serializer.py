from contentmanagement.models import Library
from contentmanagement.serializers.base_token_serializer import BaseTokenSerializer


class LibrarySerializer(BaseTokenSerializer):
    user_field_name = 'user'

    def to_representation(self, instance):
        data = super(LibrarySerializer, self).to_representation(instance)
        user = instance.user
        data['user'] = {
            'id': user.pk,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name
        }
        return data

    class Meta:
        model = Library
        fields = (
            'id',
            'name',
            'description',
            'type',
            'user',
            'created',
            'modified',
        )

        read_only_fields = ('token', 'id', 'created')
