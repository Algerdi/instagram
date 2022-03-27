from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import User, Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.prefetch_related('allComments').all()
    serializer_class = PostSerializer


class CommentViewSet(CreateModelMixin,
                     RetrieveModelMixin,
                     DestroyModelMixin,
                     ListModelMixin,
                     GenericViewSet,):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['p_pk'])

    def get_serializer_context(self):
        return {'post_id': self.kwargs['p_pk']}
