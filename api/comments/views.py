
from rest_framework.viewsets import ModelViewSet
from .models import Comment
from .serializers import SimpleCommentSerializer, CommentSerializer, LikeSerializer
from rest_framework.response import Response
from rest_framework import status



class CommentViewSet(ModelViewSet):
    
    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['p__pk']).select_related('author')

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['p__pk']).\
            select_related('author')

    def get_serializer_context(self):
        return {'post_id': self.kwargs['p__pk'], 'comment_author_id': self.request.user.id }

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentSerializer
        elif self.request.method == 'PUT':
            return LikeSerializer
        elif self.request.method == 'DELETE':
            return Response(status=status.HTTP_204_NO_CONTENT)
        return SimpleCommentSerializer

