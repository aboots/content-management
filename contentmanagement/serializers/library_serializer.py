import json

from contentmanagement.models import Library
from contentmanagement.serializers.base_token_serializer import BaseTokenSerializer


class LibrarySerializer(BaseTokenSerializer):
    user_field_name = 'owner'

    def to_representation(self, instance):
        data = super(LibrarySerializer, self).to_representation(instance)
        user = instance.owner
        data[self.user_field_name] = {
            'id': user.pk,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name
        }
        ls = []
        for user in instance.users.all():
            ls.append({
                'id': user.pk,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name
            })
        data['users'] = ls
        data['file_attributes'] = json.loads(data['file_attributes'])
        return data

    def to_internal_value(self, data):
        if hasattr(data, '_mutable') and not getattr(data, '_mutable'):
            setattr(data, '_mutable', True)
        if 'file_attributes' in data:
            data['file_attributes'] = json.dumps(data['file_attributes'])
        if 'users' not in data and 'user' in self.context:
            data['users'] = [self.context['user']]
        return super(LibrarySerializer, self).to_internal_value(data)

    class Meta:
        model = Library
        fields = (
            'id',
            'name',
            'description',
            'type',
            'owner',
            'file_attributes',
            'users',
            'created',
            'modified',
        )

        read_only_fields = ('id', 'created')
