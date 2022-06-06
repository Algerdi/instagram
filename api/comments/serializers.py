from attr import field
from rest_framework import serializers
from .models import Comment
from user.models import NewUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = [ 'user_name', 'avatar']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'comment', 'time',  ]
        read_only_fields = ['author']

    def create(self, validated_data):
        post_id = self.context['post_id']
        author_id = self.context['comment_author_id']
        return Comment.objects.create(post_id=post_id, author_id=author_id, **validated_data)

class SimpleCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ['id' ,'author', 'comment', 'total_likes', 'time']

class LikeSerializer(serializers.ModelSerializer):
    def validate(self, data):
            for user in data['likes']:
                currentUser = self.context['comment_author_id']
                if user.id != currentUser:
                    raise serializers.ValidationError(
                    'Not a user')
            return data

    class Meta:
        model = Comment
        fields = ['likes']