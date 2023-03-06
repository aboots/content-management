from django.contrib.auth import password_validation
from rest_framework import serializers

from contentmanagement.models import User
from contentmanagement.serializers import DynamicFieldModelSerializer


class UserSerializer(DynamicFieldModelSerializer):

    def to_representation(self, instance):
        data = super(UserSerializer, self).to_representation(instance)
        if 'password' in data:
            data.pop('password')
        return data

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
            'email',
            'token',
        )

        read_only_fields = ('token', 'id', 'created')

    @staticmethod
    def validate_password(password):
        password_validation.validate_password(password)
        return password


class ListUserSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        raise serializers.ValidationError('قادر به ویرایش کاربران به صورت گروهی نیستید.')

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'token',
        )

        read_only_fields = ('token', 'id', 'created')
