from rest_framework import serializers
from .models import  TaggedItem

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaggedItem
        fields = ['id', 'tag','object_id']
        read_only_fields = ['id', 'object_id']

    tag = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name= 'tp',
    )