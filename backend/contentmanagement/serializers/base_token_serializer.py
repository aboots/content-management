from contentmanagement.serializers import DynamicFieldModelSerializer


class BaseTokenSerializer(DynamicFieldModelSerializer):
    user_field_name = None

    def to_internal_value(self, data):
        if hasattr(data, '_mutable') and not getattr(data, '_mutable'):
            setattr(data, '_mutable', True)
        if 'user' in self.context:
            data[self.user_field_name] = self.context['user']
        return super(BaseTokenSerializer, self).to_internal_value(data)