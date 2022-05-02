from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import User, Post, Comment
from .serializers import SimpleCommentSerializer, UserSerializer, PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status


class PostViewSet(ModelViewSet):
    queryset = Post.objects.prefetch_related('allComments__author').all()
    serializer_class = PostSerializer


class CommentViewSet(CreateModelMixin,
                     RetrieveModelMixin,
                     DestroyModelMixin,
                     ListModelMixin,
                     GenericViewSet,):

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['p_pk']).select_related('author')

    def get_serializer_context(self):
        return {'post_id': self.kwargs['p_pk']}

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentSerializer
        elif self.request.method == 'DELETE':
            return Response(status=status.HTTP_204_NO_CONTENT)
        return SimpleCommentSerializer
