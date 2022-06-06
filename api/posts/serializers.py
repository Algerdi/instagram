from rest_framework import serializers
from tags.serializers import TagSerializer
from tags.models import TaggedItem
from .models import Post
from comments.serializers import SimpleCommentSerializer
from user.models import NewUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserSerializerExpanded(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = [ 'user_name', 'name','avatar',]

class PostSerializerNoLikes(serializers.ModelSerializer):
    """
    Is used when the post is created (POST method)
    (no ability to like, save, or give a tag)
    """
    class Meta:
        model = Post
        fields = ['id','image' ,'video', 'postContent', 'author']
        read_only_fields = ['author']
        permission_classes = (IsAuthenticatedOrReadOnly)

    def create(self, validated_data):
        author_id = self.context['post_author_id']
        return Post.objects.create(author_id=author_id, **validated_data)

class PostSerializer(serializers.ModelSerializer):
    """
    Is used when the post is updated (PUT method) if the user is an author of a post 
    (updates a post itself and gives the ability to like, save, or give a tag)
    """
    class Meta:
        model = Post
        fields = ['id','image' ,'video', 'postContent', 'author', 'likes', 'saveSystem', 'tags_label']
        read_only_fields = ['author']
        permission_classes = (IsAuthenticatedOrReadOnly)

    def validate(self, data):
        for user in data['likes']:
            currentUser = self.context['user']
            if user.id != currentUser.id:
                raise serializers.ValidationError(
                'Not a user')
            for user in data['saveSystem']:
                if user.id != currentUser.id:
                    raise serializers.ValidationError(
                    'Not a user')
                if data['tags_label'] != '':
                    post_id = self.context['pk']['pk']
                    tag_label = data['tags_label']
                    allPostTags = TaggedItem.objects.get_tags_for(Post, post_id)
                    tags_list = []
                    for tag in allPostTags:
                        tags_list.append(tag.tag)
                    if tag_label not in tags_list:
                        TaggedItem.objects.create_tags(Post,post_id, tag_label )
        return data


class PostSerializerView(serializers.ModelSerializer):
    """
    Is used with GET method to show all posts
    """
    tags = TagSerializer(required=False, many=True)
    allComments = SimpleCommentSerializer(
        many=True, required=False, read_only=True)
    author = UserSerializerExpanded()
    class Meta:
        model = Post
        fields = ['id' ,'image', 'video', 'postContent', 'author', 'tags',  'total_likes', 'likes','saveSystem', 'allComments']


class LikeSaveSerializer(serializers.ModelSerializer):
    """
   Is used when the post is updated (PUT method) if the user is NOT an author of a post 
   (gives the ability to like and save the post)
    """
    def validate(self, data):
        for user in data['likes']:
            currentUser = self.context['user']
            if user.id != currentUser.id:
                raise serializers.ValidationError(
                'Not a user')
            for user in data['saveSystem']:
                if user.id != currentUser.id:
                    raise serializers.ValidationError(
                    'Not a user')
        return data

    class Meta:
        model = Post
        fields = ['likes', 'saveSystem']

class SavedPostsSerializer(serializers.ModelSerializer):
    """
    Is used to get (GET method) all saved posts of a particular user
    """
    tags = TagSerializer(required=False, many=True)
    class Meta:
        model = Post
        fields = ['id', 'image', 'video', 'postContent', 'tags']
        read_only_fields = ['id', 'postContent', 'saveSystem']


    # interesting method
    # likes1 = serializers.SerializerMethodField(method_name='likes')
    # def likes(self, post:Post):
    #     user = self.context['post_author_id']
    #     pk  = self.context['pk']
    #     like = post.likes.through.objects.get(post_id=pk['pk'], newuser_id=user)
    #     user_id = like.newuser_id
    #     print(user_id)
    #     return user_id


    # def update(self, instance,validated_data):
    #     if validated_data['tags_label'] != '':
    #         TaggedItem.objects.create_tags(Post, instance.id, validated_data['tags_label'])
    #         instance.save()
    #         return instance
    #     else:
    #         return instance

    # def update(self, instance,validated_data):
    #     print(instance)
    #     print(validated_data)
    #     if validated_data['tags_label'] != '':
    #         TaggedItem.objects.create_tags(Post, instance.id, validated_data['tags_label'])
    #         m2m_fields = [instance.likes, instance.saveSystem]
    #         print(m2m_fields)
    #         for attr, value in m2m_fields:
    #             field = getattr(instance, attr)
    #             field.set(value)
    #         instance.save()
    #         return instance
    #     else:
    #         return instance

    # def create(self, validated_data):
    #     print(validated_data)
    #     if validated_data['tags_label'] != '':
    #         post = self.context['pk']
    #         tag = TaggedItem.objects.create_tags(Post, post['pk'], validated_data['tags_label'])
    #         print(tag)
    #         return Post.objects.create(tags_label=tag)
    #     else:
    #         return validated_data

