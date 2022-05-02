from cmath import isnan
from rest_framework import serializers
from .models import Post, Comment
from user.models import NewUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = [ 'user_name', 'avatar']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'author', 'comment', 'time']

    def create(self, validated_data):
        post_id = self.context['post_id']
        return Comment.objects.create(post_id=post_id, **validated_data)


class SimpleCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ['author', 'comment', 'time']


class PostSerializer(serializers.ModelSerializer):
    allComments = SimpleCommentSerializer(
        many=True, required=False)

    class Meta:
        model = Post
        fields = ['id', 'postContent', 'allComments']
