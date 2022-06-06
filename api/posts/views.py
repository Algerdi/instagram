from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, mixins, GenericViewSet
from tags.models import TaggedItem
from tags.serializers import TagSerializer
from .models import Post
from .serializers import PostSerializer, PostSerializerNoLikes, PostSerializerView, LikeSaveSerializer,SavedPostsSerializer
from  rest_framework.views import APIView

class PostViewSet(ModelViewSet):

    def get_queryset(self):
        return Post.objects.select_related('author').\
        prefetch_related('allComments__author').\
        prefetch_related('likes').\
        prefetch_related('saveSystem').\
        prefetch_related('tags')

    def get_serializer_context(self):
        return {'post_author_id': self.request.user.id, 
                'user':self.request.user,
                'pk': self.request.parser_context.get('kwargs'),
                'request': self.request
                }

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostSerializerView
        elif self.request.method == 'PUT': 
            pk  = self.request.parser_context.get('kwargs')
            post = Post.objects.get(id = pk['pk'])
            if self.request.user.id != post.author_id: 
                return LikeSaveSerializer 
            else: 
                return PostSerializer
        elif self.request.method == 'DELETE':
            return Response(status=status.HTTP_204_NO_CONTENT)
        return PostSerializerNoLikes

class SavedPostsView(ReadOnlyModelViewSet):
    serializer_class = SavedPostsSerializer
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(saveSystem = user.id).\
            select_related('author').\
            prefetch_related('tags')

class TagViewSet(ReadOnlyModelViewSet):
    serializer_class = TagSerializer
    queryset = TaggedItem.objects.all()

class MyTagsViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = TagSerializer
    def get_queryset(self):
        user = self.request.user
        all_posts_user_tagged  = Post.objects.filter(author = user)
        id_list = []
        for post in all_posts_user_tagged:
            id_list.append(int(post.id))
        return TaggedItem.objects.filter(object_id__in = id_list).select_related('content_type')

class TaggedPostsViewSet(APIView):
    def get(self, request, pk):
        id_list = TaggedItem.objects.get_id_list(Post,pk)
        Post.objects.filter(id__in = id_list)
        queryset = Post.objects.filter(id__in = id_list).\
                select_related('author').\
                prefetch_related('allComments__author').\
                prefetch_related('likes').\
                prefetch_related('saveSystem').\
                prefetch_related('tags')
        serializer = PostSerializerView(queryset, many=True, context={'request': request})
        return Response(serializer.data)


# def perform_create(self, serializer):
#     serializer.save()
# def update(self, request, *args, **kwargs):
#     pers = request.user.id
#     post = Post.objects.get(id = kwargs['pk'])
#     if pers == post.author.id:
#         partial = kwargs.pop('partial', True)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif pers != post.author.id:
#         # serializer = LikeSerializer(data=request.data)
#         # serializer.is_valid(raise_exception=True)
#         # serializer.save()
#         # return Response(serializer.data)
#         return Response({'error': 'Not an author'},status=status.HTTP_405_METHOD_NOT_ALLOWED)

