from rest_framework import serializers
from .models import NewUser


class NewUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewUser
        fields = ('id', 'email', 'user_name', 'gender',
                  'name', 'avatar', 'phone_number',
                  'website', 'start_date', 'bio')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
