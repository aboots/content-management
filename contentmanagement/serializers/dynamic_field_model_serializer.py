from rest_framework.serializers import ModelSerializer


class DynamicFieldModelSerializer(ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.context:
            return
        request = self.context.get('request')
        if (not request) or str(request.method).lower() != 'get':
            return
        fields = request.query_params.getlist('fields')
        if not fields:
            return
        inquired = set(fields)
        existing = set(self.fields.keys())
        for field_name in existing - inquired:
            self.fields.pop(field_name)
